import serial
import time


class RCController():

    def __init__(self):
        '''
        Create a rc controller that connects to a arduino providing pwm signals via serial
        '''

        print('Starting RC controller...')

        self.angle = 0.0
        self.throttle = 0.0
        self.mode = 'user'
        self.recording = True
        self.connection = serial.Serial('/dev/ttyACM0', 9600)  # todo: put this to config
        time.sleep(5)  # Arduino is resetting
        print('Established connection to Arduino')

    def update(self, port=8887):
        None

    def run_threaded(self, img_arr=None):
        try:
            response = self.connection.readline()
            responseline = response.decode('utf-8')
            responselist = responseline.split(":")
            if len(responselist) > 2:
                if responselist[0] == "chunk":
                    self.angle = float(responselist[2]) / 100
                    self.throttle = float(responselist[1]) / 100
            self.controller.flushinput()
        except KeyboardInterrupt:
            print('Interrupt error reading from arduino')
        except:
            print('any other error reading from arduino')
        self.img_arr = img_arr
        return self.angle, self.throttle, self.mode, self.recording

    def run(self, img_arr=None):
        try:
            response = self.connection.readline()
            responseline = response.decode('utf-8')
            responselist = responseline.split(":")
            if len(responselist) > 2:
                if responselist[0] == "chunk":
                    self.angle = float(responselist[2]) / 100
                    self.throttle = float(responselist[1]) / 100
            self.controller.flushinput()
        except KeyboardInterrupt:
            print('Interrupt error reading from arduino')
        except:
            print('any other error reading from arduino')
        self.img_arr = img_arr
        return self.angle, self.throttle, self.mode, self.recording