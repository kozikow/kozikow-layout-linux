#!/usr/bin/python
import subprocess
import threading
import os
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
            subprocess.call(["xmodmap", os.path.join(os.getcwd(), "layeron.xmodmap")])
          elif event.value == KEY_UP:
            subprocess.call(["xmodmap", os.path.join(os.getcwd(), "layeroff.modmap")])


if __name__ == "__main__":
  for filename in os.listdir(DEVICE_ROOT):
    if "event" in filename:
      full_path = os.path.join(DEVICE_ROOT, filename)
      print full_path
      thread = RemapperThread(full_path)
      thread.start()
