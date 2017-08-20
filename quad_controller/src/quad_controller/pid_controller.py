# Copyright (C) 2017 Electric Movement Inc.
# All Rights Reserved.

# Author: Brandon Kinman


class PIDController:
    def __init__(self, kp = 0.0, ki = 0.0, kd = 0.0, max_windup = 10):
        #TODO
        self.kp_ = float(kp)
        self.ki_ = float(ki)
        self.kd_ = float(kd)
        self.max_windup_ = float(max_windup)

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
        self.target_ = float(target)

    def setKP(self, kp):
        #TODO
        self.kp_ = float(kp)

    def setKI(self, ki):
        #TODO
        self.ki_ = float(ki)

    def setKD(self, kd):
        #TODO
        self.kd_ = float(kd)

    def setMaxWindup(self, max_windup):
        #TODO
        self.max_windup_ = float(max_windup)

    def update(self, measured_value, timestamp):
        #TODO
        delta_time = timestamp - self.last_timestamp_
        if delta_time == 0:
            # Delta time is zero
            return 0
        
        # Calculate the error 
        error = self.target_ - measured_value
        
        # Set the last_timestamp_ 
        self.last_timestamp_ = timestamp

        # Sum the errors
        self.error_sum_ += error * delta_time
        
        # Update the past error
        self.last_error_ = error
        
        # Find delta_error
        delta_error = error - self.last_error_
        
        # Address max windup
        ########################################
        if self.error_sum_ > self.max_windup_:
            self.error_sum_ = self.max_windup_
        elif self.error_sum_ < -self.max_windup_:
            self.error_sum_ = -self.max_windup_

        ########################################
        
        # Proportional error
        p = self.kp_ * error
       
        # Integral error
        i = self.ki_ * self.error_sum_
       
        # Recalculate the derivative error here incorporating 
        # derivative smoothing!
        ########################################
        #filtered = self.previous_filtered + self.alpha*(measured_value - self.previous_filtered)
        #filtered_error = self.set_point_ - filtered
        #delta_error = (filtered_error - self.last_error_) / delta_time
        #d = self.kd_ * delta_error
        d = self.kd_ * (self.alpha * delta_error / delta_time + (1 - self.alpha))
        #self.previous_filtered = filtered
        ########################################
        
        # Set the control effort
        u = p + i + d
        
        # Enforce actuator saturation limits
        ########################################

        #if u > self.umax:
        #    u = self.umax
        #elif u < self.umin:
        #    u = self.umin


        ########################################
    
        # Here we are storing the control effort history for post control
        # observations. 
        #self.u_p.append(p)
        #self.u_i.append(i)
        #self.u_d.append(d)

        return u


