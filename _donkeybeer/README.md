# TODO
 
 (systematisches Fehler analysieren nochmal nachschlagen)
 
* Rebase from upstream
* Mobilenetv2
* Alternativ: Fully connected layer per output
* anfahren nach und nach (ESC verträgt kein Max Auschlag zu Beginn)
* Transfer Learning resnet 50 abschließen
    * see slack maybe its possible to change simulator resolution
* Tensorboard callback mehr metriken anschalten und durchtesten
* Organize logs in subfolder (generate from current Time & ModelType)
* Run on Kubeflow..? (No idea if Keras supports this): github.com/kubeflow/examples/issues/48
* Data Augmentation on images (see kaggle)
* calibrate rc controller (see rc.py, donkey2.py and config_defaults.py)
    * test Choose mode in UI:
    * User: User controls all
    * Local Angle: AI controls Angle
    * Local Throttle & Angle: AI controls Throttle & Angle
* http://www.donkeycar.com/updates
* Reuse already calculated models (multiple models? & then average?)
* Tune hyperparameter
    * Increase Camera Resolution => But maybe too much data for Raspberry
    * Batchsize 
    * Train/Validation Split
    * Overfitting:
        * Regularization: Increase Dropout
        * More data
    * Underfitting:
        * Regularization: Decrease Dropout
        * Layers
            * Conv2D => Padding Same?
            * Max Pooling    
        * More Params
    * loss_weights?    


# ssh on donkeycar

````
donkeyssh
````

# Update, compile & start donkeycar on donkeycar

````
donkeycompile && donkeystart
# UI: http://donkeybeer:8887/drive
````

# Install donkeycar on Fedora

```
sudo dnf install -y python3-virtualenv

cd /home/fedora/code/github.com/wroscoe/donkey
virtualenv-3 env -p python3
source env/bin/activate
pip install keras==2.0.6
pip install tensorflow==1.3.0
pip install -e donkeycar
````

# Initial Setup on donkeycar


## Screen

````
apt-get install screen
````

## RC Controller Setup on donkeycar

Based on https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/

````
ssh pi@$donkeybeer
# PW asdfasdf

# Setup
pip install pyserial

# Debug
sudo apt-get install python-serial
python
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
while 1 :
    ser.readline()
````

## PS3 Controller Setup on donkeycar

Based on https://pythonhosted.org/triangula/sixaxis.html

````
ssh pi@$donkeybeer
# PW asdfasdf

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

# Setup Simulator

Download and extract simluator (http://docs.donkeycar.com/guide/simulator/) to $DONKEY_HOME/DonkeySimLinux.