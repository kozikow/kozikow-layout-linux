#!/bin/sh
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install git gcc make pkg-config libx11-dev libxtst-dev libxi-dev

git clone https://github.com/alols/xcape.git
cd xcape
make
sudo make install
cd ..
rm -r xcape

# latest development version of evdev. Stable version didn't work for me.
# In case of errors check out http://pythonhosted.org/evdev/install.html
pip install git+git://github.com/gvalkov/python-evdev.git

pip install pyinotify
pip install sh
pip install pyudev
pip install evdev
