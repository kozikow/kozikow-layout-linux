import os
import pyinotify
import threading

LAYER_KEY = 126 # Right windows key
KEY_DOWN = 1
KEY_UP = 0
DEVICE_ROOT = "/dev/input/"

thread_info_lock = threading.Lock()
device_path_to_thread = {}

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
  wm = pyinotify.WatchManager()
  mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO | pyinotify.IN_MOVED_FROM | pyinotify.IN_MODIFY
  handler = EventHandler()
  notifier = pyinotify.Notifier(wm, handler)
  wm.add_watch(DEVICE_ROOT, mask, rec=True)
  notifier.loop()


def on_new_device_found(path):
  print "New Device: %s" % path
  user_id = os.getuid()
  os.chown(path,  user_id, -1)
  full_path = os.path.join(DEVICE_ROOT, path)
  os.chown(full_path, user_id, -1)
#   todo: initial keymaps
#   todo: layers


if __name__ == "__main__":
  for filename in os.listdir(DEVICE_ROOT):
    if "event" in filename:
      full_path = os.path.join(DEVICE_ROOT, filename)
      on_new_device_found(full_path)
  init_pyinotify()
