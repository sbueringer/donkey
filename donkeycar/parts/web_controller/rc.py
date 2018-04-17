import serial
import time
import math

class RCController():

    def __init__(self, forward_throttle=100.0,
                 stopped_throttle=0.0,
                 tolerance_range_throttle=3.0,
                 reverse_throttle=-93.0,
                 left_steering=93.0,
                 center_steering=0.0,
                 tolerance_range_steering=3.0,
                 right_steering=110.0):
        '''
        Create a rc controller that connects to a arduino providing pwm signals via serial
        '''

        print('Starting RC controller...')

        self.angle = 0.0
        self.throttle = 0.0
        self.forward_throttle = forward_throttle
        self.stopped_throttle = stopped_throttle
        self.tolerance_range_throttle = tolerance_range_throttle
        self.reverse_throttle = reverse_throttle
        self.range_throttle = forward_throttle - reverse_throttle
        self.left_steering = left_steering
        self.center_steering = center_steering
        self.tolerance_range_steering = tolerance_range_steering
        self.right_steering = right_steering
        self.range_steering = right_steering - left_steering
        self.mode = 'user'
        self.recording = True
        self.connection = serial.Serial('/dev/ttyACM0', 115200)  # todo: put this to config
        time.sleep(5)  # Arduino is resetting
        print('Established connection to Arduino')

    def update(self, port=8887):
        None

    def run_threaded(self, img_arr=None):
        try:
            response = self.connection.readline()
            responseline = response.decode('utf-8')
            responselist = responseline.split(":")
            print('RCController: Input angle: ' + str(responselist[1]) + ' throttle: ' + str(responselist[2]))
            if len(responselist) > 2:
                if responselist[0] == "chunk":
                    self.angle = self.calculateAngle(float(responselist[1]))
                    self.throttle = self.calculateThrottle(float(responselist[2]))
            print('RCController: Output angle: ' + str(self.angle) + ' throttle: ' + str(self.throttle))
            self.controller.flushinput()
        except KeyboardInterrupt:
            print('Interrupt error reading from arduino')
        except:
            ignore_exception = True
        self.img_arr = img_arr
        return self.angle, self.throttle, self.mode, self.recording

    def run(self, img_arr=None):
        try:
            response = self.connection.readline()
            responseline = response.decode('utf-8')
            responselist = responseline.split(":")
            print('RCController: Input angle: ' + str(responselist[1]) + ' throttle: ' + str(responselist[2]))

            if len(responselist) > 2:
                if responselist[0] == "chunk":
                    self.angle = self.calculateAngle(float(responselist[1]))
                    self.throttle = self.calculateThrottle(float(responselist[2]))
            print('RCController: Output angle: ' + str(self.angle) + ' throttle: ' + str(self.throttle))
            self.controller.flushinput()
        except KeyboardInterrupt:
            print('Interrupt error reading from arduino')
        except:
            ignore_exception = True
        self.img_arr = img_arr
        return self.angle, self.throttle, self.mode, self.recording

    def calculateAngle(self, rawAngle):
        if ((-self.tolerance_range_steering) <= rawAngle) and (rawAngle <= self.tolerance_range_steering):
            return 0

        if rawAngle > 0:
            return rawAngle / math.fabs(self.right_steering)
        else:
            return rawAngle / math.fabs(self.left_steering)

    def calculateThrottle(self, rawThrottle):
        if ((-self.tolerance_range_throttle) <= rawThrottle) and (rawThrottle <= self.tolerance_range_throttle):
            return 0

        if rawThrottle > 0:
            return rawThrottle / math.fabs(self.forward_throttle)
        else:
            return rawThrottle / math.fabs(self.reverse_throttle)
