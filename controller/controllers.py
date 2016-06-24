import os
import serial

class Controller():
    def __init__(self, is_motor_forwards=True):
        # Our serial to communicate with arduino
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        self.is_motor_forwards = is_motor_forwards

        self.run_speed(0)
        self.ser.write('motor-dir,' + str(int(is_motor_forwards)) + '\n')

    #### Motors ####
    # range = 0 <= x <= 100
    #
    # motor-dir: 0 = forward, 1 = backwards
    # Runs motors
    def run_speed(self, speed):
        if speed < 0:
            speed = 0
        elif speed > 100:
            speed = 100

        self.ser.write('motor,' + str(speed) + '\n')

    # Toggles direction
    def toggle_dir(self):
        self.is_motor_forwards = not self.is_motor_forwards
        self.ser.write('motor-dir,' + str(int(self.is_motor_forwards)) + '\n')

    # Stop
    def stop(self):
        self.ser.write('motor,0\n')

    #####Servo ####
    # Turns
    # range = 50 <= x <= 150
    # 50 = full right, 150 = full left
    def turn(self, val, left=True):
        if left:
            val = 100 + val
        else:
            val = 100 - val

        if val < 50:
            val = 50
        elif val > 150:
            val = 150

        self.ser.write('steer,' + str(val) + '\n')

    # Straigthens servo
    def straighten(self):
        self.ser.write('steer,100\n')

