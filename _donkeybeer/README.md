# Start car


## Alias (in .bashrc)
````
alias start='cd ~; rm -rf ~/d2; donkey createcar --template donkey2 --path ~/d2; cd ~/d2; python manage.py drive'
alias compile='cd ~/donkeycar; git pull; pip install -e .'
alias compile='cd ~/donkeycar; pip install -e .'
````

````
ssh pi@$donkeybeer
# PW asdfasdf


start
# http://192.168.43.164:8887/drive
````

# Update donkeycar on donkeycar

````
compile
````

# Install donkeycar on Linux

```

sudo dnf install -y python3-virtualenv

cd ~
#sudo apt-get install virtualenv build-essential python3-dev gfortran libhdf5-dev
virtualenv-3 env -p python3
source env/bin/activate
pip install keras==2.0.6
pip install tensorflow==1.3.0

cd /home/fedora/code/github.com/wroscoe/donkey
pip install -e donkeycar
````

# Setup


## RC Controller Setup

https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
````
ssh pi@$donkeybeer
# PW asdfasdf

## Debug
sudo apt-get install python-serial
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
while 1 :
    ser.readline()

# Setup
pip install pyserial
````

## Controller Setup


````
ssh pi@$donkeybeer
# PW asdfasdf

# https://pythonhosted.org/triangula/sixaxis.html

sudo apt-get install bluetooth libbluetooth3 libusb-dev
sudo systemctl enable bluetooth.service
sudo usermod -G bluetooth -a pi
reboot


wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
sudo ./sixpair

# Use controller:
#vi /home/pi/d2/config.py 
#USE_JOYSTICK_AS_DEFAULT = True

bluetoothctl
agent on
devices
trust <MAC ADDRESS>
default-agent
quit

ls /dev/input/js0
````

