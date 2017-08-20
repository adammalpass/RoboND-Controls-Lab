# Copyright (C) 2017 Electric Movement Inc.
# All Rights Reserved.

# Author: Brandon Kinman


class PIDController:
    def __init__(self, kp = 0.0, ki = 0.0, kd = 0.0, max_windup = 10):
        #TODO
        self.kp_ = kp
        self.ki_ = ki
        self.kd_ = kd
        self.max_windup_ = max_windup

        # Store relevant data
        self.last_timestamp_ = 0.0
        self.target_ = 0.0
        #self.start_time_ = start_time
        self.error_sum_ = 0.0
        self.last_error_ = 0.0


    def reset(self):
        #TODO
        self.target_ = 0.0
        self.kp_ = 0.0
        self.ki_ = 0.0
        self.kd_ = 0.0
        
        self.error_sum_ = 0.0
        self.last_timestamp_ = 0.0
        self.last_error_ = 0
        #self.last_last_error_ = 0
        #self.last_windup_ = 0.0

    def setTarget(self, target):
        #TODO
        self.target_ = target

    def setKP(self, kp):
        #TODO
        self.kp_ = kp

    def setKI(self, ki):
        #TODO
        self.ki_ = ki

    def setKD(self, kd):
        #TODO
        self.kd_ = kd

    def setMaxWindup(self, max_windup):
        #TODO
        self.max_windup_ = max_windup

    def update(self, measured_value, timestamp):
        #TODO
        pass


