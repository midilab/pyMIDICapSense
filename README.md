# Capacitive Sensor MIDI Controller for Raspberry(s), Odroid(s) and Cubieboard(s).

## What is pyMIDICapSense?

pyMIDICapSense is a Capacitive Sensor MIDI Controller for plataforms with Physical GPIO pins access like Raspberry(s), Odroid(s) and Cubieboard(s) writed in python.

It creates a ALSA MIDI interface capable of interact with ALSA instruments or other plugins by it self or via JACK AUDIO KIT MIDI routing(in this case select alsa seq as MIDI driver for Jack). 

It was primarily writed for a [interactive instalation project](http://midilab.co/water-oracle/) and goes to anyone that can find this usefull. Under MIT license.

With pyMIDICapSense you can:

1. Turn nearly everything you could imagine, like water cup, fruits or your pet into a touchable MIDI Controller.
2. Transform your touches into MIDI Commands to interact with instruments or plugins. For now only MIDI Notes are supported.
3. Configure each Capacitive Sensor to be trigguered into 4 different modes: 
*RANDOM*: you create a list of (n) MIDI notes for a sensor and each touch it will send a random MIDI note within the list.
*SEQUENTIAL*: you create a list of (n) MIDI notes for a sensor and each touch it will send the (n)+1 MIDI note within the list.
*BANK_SELECT*: you create more than one BANK to handle more complex setups. you create a list of (n) MIDI notes for a sensor and each touch it will send the selected BANK (n) MIDI note within the list.
*BANK_CHANGE*: you setup the sensor as a functional touchable BANK changer.
4. Configure a user feedback for each sensor. Eg. On each sensor touch, ligth a LED or Start a engine. 


## Installation

RTMIDI and wiringPI2 are required to run this project

**Dependencies**
On Debian/Ubuntu
```bash
sudo apt-get install build-essential python-dev python-pip python-setuptools libasound-dev git libjack-dev
```

On Archlinux
```bash
sudo pacman -S base-devel python python-pip python-setuptools git alsa-lib
```

**RTMidi for python**
Install via pip
```bash
sudo pip install --pre python-rtmidi
```

**WiringPI2 for python**

[Raspberry](https://github.com/Gadgetoid/WiringPi2-Python/)

Compile WiringPI C version
```bash
git clone git://git.drogon.net/wiringPi; cd wiringPi; sudo ./build
```

Compile the WiringPI2 python version
```bash
git clone https://github.com/Gadgetoid/WiringPi2-Python.git; cd WiringPi2-Python; sudo python setup.py install
```

[Cubieboard](https://github.com/gootoomoon/WiringCB-python/)

Compile the WiringPI C and python version once
```bash
git clone https://github.com/gootoomoon/WiringCB-python.git; cd WiringCB-python; sudo python setup.py install
```

[ODROID-C1](https://github.com/mlinuxguy/WiringPi2-odroid-c1/)
 
Compile WiringPI C version
```bash
git clone git://git.drogon.net/wiringPi; cd wiringPi; sudo ./build
```

Compile the WiringPI2 python version
```bash
git clone https://github.com/Gadgetoid/WiringPi2-Python.git; cd WiringPi2-Python; sudo python setup.py install
```

## Usage

Configure your sensors

1. How many sensor are you going to use?
2. Do you want to make usage of BANKS for more complex setups?
3. Do you feel good about a user feedback for each sensor?

After answer those questions use the config.py to setup your sensors, inside this file you have a example used for the [interactive instalation water oracle](http://midilab.co/water-oracle/), you can use it as basis for your own. 

After all, run pyMIDICapSense.py
```bash
python pyMIDICapSense.py
```

**Full details at:**
http://midilab.co/projects/pymidicapsense/

