"""rumba_controller controller."""

# @Author: Manvir Saini

import math
from controller import Robot

# Last update March 14, 2021
#TODO:
    
class Rumba_controller:
    # create the Robot instance.
    
    robot = Robot()
        
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
            
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
            
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
        
    # Robot attributes
    timestep = 64
    max_speed = 16.129 # angular speed
    turn_speed = 5.0 # angular speed
    wheel_radius = 0.031
    axle_length = 0.271756
    linear_velocity = wheel_radius * max_speed
            
    # Rotation for 90 degree (angular) 
    angle_of_rotation = 6.28/4 # angular 90 degrees
    rate_of_rotation = (linear_velocity)/axle_length
    turn_time = 1.7 * (angle_of_rotation / rate_of_rotation)
    
    #Record the rotation of the bot
    turns = []
    
    # Robot movement functions
    # Move forward for a certain amount of blocks
    def move_forward(self, blocks):
    
        start_time = self.robot.getTime() 
        block_distance = 1.0
        
        drive_time = (blocks * block_distance)/ self.linear_velocity
        
        while self.robot.step(self.timestep) != -1:
        
            current_time = self.robot.getTime()
            
            if(current_time >= start_time + drive_time):

                left_speed = 0
                right_speed = 0
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                break
            else:
                left_speed = self.max_speed
                right_speed = self.max_speed
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
        pass
 
     
    #Spin right 
    def move_right(self):
        
        self.turns.append('right')
        
        start_time = self.robot.getTime() 
        
        while self.robot.step(self.timestep) != -1:
        
            current_time = self.robot.getTime()

            if current_time >= start_time + self.turn_time:
                left_speed = 0
                right_speed = 0
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                break
            else:
                left_speed = -self.turn_speed
                right_speed = self.turn_speed
            
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
        pass
        
    #Spin left
    def move_left(self):
        
        self.turns.append('left')
    
        start_time = self.robot.getTime() 
        
        while self.robot.step(self.timestep) != -1:
        
            current_time = self.robot.getTime()

            if current_time >= start_time + self.turn_time:
                left_speed = 0
                right_speed = 0
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                break
            else:
                left_speed = self.turn_speed
                right_speed = -self.turn_speed
            
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
        pass

    #Move backwards indefinitely
    def move_backward(blocks):
    
        start_time = self.robot.getTime() 
        block_distance = 1.0
        
        drive_time = (blocks * block_distance)/ self.inear_velocity
        
        while self.robot.step(self.timestep) != -1:
        
            current_time = self.robot.getTime()
            
            if(current_time >= start_time + self.drive_time):
                left_speed = 0
                right_speed = 0
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                break
            else:
                left_speed = -self.max_speed
                right_speed = -self.max_speed
                
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
        pass
        
    # Face the robot north 
    def face_north(self):
        
        if (len(self.turns) == 0):
            pass
        else:
            
            if (len(self.turns) > 2):
                if (self.turns[-1] == 'left' 
                and self.turns[-2] == 'left' 
                and self.turns[-3] == 'left'):
            
                    self.move_left()
                
            elif (len(self.turns) > 1): 
                if(self.turns[-1] == 'left' and self.turns[-2] == 'left'):
                    self.move_right()
                    self.move_right()
               
            elif (self.turns[-1] == 'left'):
                self.move_right()
                
            elif (len(self.turns) > 2):
                if(self.turns[-1] == 'right' 
                and self.turns[-2] == 'right' 
                and self.turns[-3] == 'right'):
                
                    self.move_right()
                
            elif (len(self.turns) > 1): 
                if(self.turns[-1] == 'right' and self.turns[-2] == 'right'):
                    self.move_left()
                    self.move_left()
                
            else:
                self.move_right()
                
            self.turns.clear()

#TEST
