#!/bin/sh
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install python-dev
sudo apt-get install python-pip


# latest development version of evdev. Stable version didn't work for me.
# In case of some errors check out http://pythonhosted.org/evdev/install.html
pip install git+git://github.com/gvalkov/python-evdev.git

pip install pyinotify
pip install sh


