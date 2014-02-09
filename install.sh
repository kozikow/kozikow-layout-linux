#!/bin/sh
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install python-dev
sudo apt-get install python-pip


git clone https://github.com/alols/xcape.git
cd xcape
make
sudo cp xcape /bin/
cd ..


# latest development version of evdev. Stable version didn't work for me.
# In case of some errors check out http://pythonhosted.org/evdev/install.html
pip install git+git://github.com/gvalkov/python-evdev.git

pip install pyinotify
pip install sh
pip install pyudev
pip install evdev
