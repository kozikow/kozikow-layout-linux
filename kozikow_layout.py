import pyinotify
import subprocess
import threading
import os
import re
import signal

import sh

from evdev import InputDevice, ecodes


LAYER_KEY = 126 # Right windows key
KEY_DOWN = 1
KEY_UP = 0
DEVICE_ROOT = "/dev/input/"


class RemapperThread(threading.Thread):
  def __init__(self, path):
    threading.Thread.__init__(self)
    self.path = path

  def run(self):
    dev = InputDevice(self.path)
    for event in dev.read_loop():
      if event.type == ecodes.EV_KEY and event.code == LAYER_KEY:
        if event.value == KEY_DOWN:
          subprocess.call(
            ["xmodmap", os.path.join(os.getcwd(), "layeron.xmodmap")])
        elif event.value == KEY_UP:
          subprocess.call(
            ["xmodmap", os.path.join(os.getcwd(), "layeroff.xmodmap")])


class EventHandler(pyinotify.ProcessEvent):
  def process_IN_CREATE(self, event):
    path = os.path.join(event.path, event.name)
    on_new_device_found(path)

  def process_IN_MODIFY(self, event):
    path = os.path.join(event.path, event.name)
    on_new_device_found(path)

  def process_IN_MOVED_TO(self, event):
    path = os.path.join(event.path, event.name)
    on_new_device_found(path)


def init_pyinotify():
  """
  Starts a notifiation system that gets notification when something relevant
  in DEVICE_ROOT changes.
  """
  wm = pyinotify.WatchManager()
  mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO | \
         pyinotify.IN_MOVED_FROM | pyinotify.IN_MODIFY
  handler = EventHandler()
  notifier = pyinotify.Notifier(wm, handler)
  wm.add_watch(DEVICE_ROOT, mask, rec=True)
  notifier.loop()


def get_list_of_pids_matching_regex(regex):
  process_lines = re.findall(regex, "\n".join(sh.ps("cax")))
  return [int(line.split()[0]) for line in process_lines if len(line) > 0]


def kill_processes_matching_regex(regex):
  pids = get_list_of_pids_matching_regex(regex)
  for pid in pids:
    try:
      os.kill(pid, signal.SIGTERM)
    except OSError:
      print "Killing process with pid %d (name matches regex %s) gently (" \
            "SIGTERM) failed. sending SIGKILL. " % (regex, pid)
      os.kill(pid, signal.SIGKILL) # If this fails whole function throws
  assert (len(get_list_of_pids_matching_regex(regex)) == 0)


def run_xcape():
  """
  Start a daemon that is adding functionality of esc to caps lock, ctrl to
  enter and backspace to shift.
  It is only needed to run it once, since xcape picks up new devices by itself.
  Two instances of xcape mess with everything
  """
  os.system(
    "xcape -e \"$spare_modifier=Return;Control_L=Escape;Shift_R\=BackSpace\""
  )


def on_new_device_found(path):
  """
  Function to run when the new keyboard input device is found.
  Loads initial map and starts a thread that is making LAYER_KEY a layer key
  @param path: Path to input device. Subfile of DEVICE_ROOT
  """
  print "New Device: %s" % path
  user_id = os.getuid()
  os.chown(path, user_id, -1)
  full_path = os.path.join(DEVICE_ROOT, path)
  os.chown(full_path, user_id, -1)
  subprocess.call(
    ["xmodmap", os.path.join(os.getcwd(), "initial.xmodmap")])
  thread = RemapperThread(path)
  thread.start()


def reset_to_default_layout():
  """
  This just in case tries to bring system to clean state
  """
  os.system("setxkbmap -layout us")
  kill_processes_matching_regex(".*xcape.*")
  kill_processes_matching_regex(".*kozikow_layout.py.*")


if __name__ == "__main__":
  reset_to_default_layout()
  for filename in os.listdir(DEVICE_ROOT):
    if "event" in filename:
      full_path = os.path.join(DEVICE_ROOT, filename)
      on_new_device_found(full_path)
  init_pyinotify()
  run_xcape()
