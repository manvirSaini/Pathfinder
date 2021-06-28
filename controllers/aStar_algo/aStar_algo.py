"""aStar_algo controller."""

# @Author: Manvir Saini

import math
# Bring other packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'rumba_controller')))
sys.path.append(os.path.abspath(os.path.join('..', 'board_controller')))

from rumba_controller import Rumba_controller
from board_controller import Board_controller


# This class will use A_star to mark a path for the robot to 
# follow. It does not keep a list of nodes to visit, but rather will
# mark the path along the way until the target is met; since the board
# controller class is handling the movement of the robot.

class A_star:
    
    rumba = Rumba_controller()
    board_cont = Board_controller()
    
    # create the Robot and Board instance.
    robot = rumba.robot
    board = board_cont.org_board.copy() # Get board form board controller
    
    # Set coordinates of the target value
        #Simulation1
    # target_x, target_y = (0,0)
    
        #Simulation2
    # target_x, target_y = (0,2)
    
        #Simulation3
    target_x, target_y = (2,6)
    
    
    # Set coordinates of the start value 
    # start_x, start_y = (board_cont.position_x, board_cont.position_y)
    start_x, start_y = (9, 9)
    
    # Set coordinates of the current value
    position_x, position_y = (9, 9)
    
    # Marker to create path (only integer working rn)
    mark = 4
    
    # This method will return a heuristic value for
    #  the expected distance from target 
    def H(self, x, y):
        
        if x == self.target_x and y == self.target_y:
            return 0
            
        elif self.board[y][x] == -1:
            return math.inf
 
        else:
            # Using euclidean distance, I think
            y_diff = y - self.target_y
            x_diff = x - self.target_x
            h = math.sqrt((x_diff ** 2) + (y_diff ** 2))

            return h 
        
    # This method will mark the path on the board
    def path_maker(self):
        
        #Running until robot is one block away from target
        while self.board[self.position_y-1][self.position_x] != 1 and self.board[self.position_y][self.position_x-1] != 1:

           self.mark_point()
       
        self.board_cont.print_board(self.board)
        self.board_cont.follow_path(self.board, self.mark)
        
    
    
    # This mehtod will mark the block above current
    def mark_up(self):
         #Check if better than current block 
        if self.H(self.position_x, self.position_y-1) < self.H(self.position_x, self.position_y):
            
            self.board[self.position_y-1][self.position_x] = self.mark
            self.position_y = self.position_y-1
        
        else:
            # Will also be in infinite while loop
            self.terminator('up')   
            
          
    # This method will mark the block to left of current            
    def mark_left(self):
        # Not needed but just confirming
        if self.H(self.position_x-1, self.position_y) < self.H(self.position_x, self.position_y):
            
            self.board[self.position_y][self.position_x-1] = self.mark
            self.position_x = self.position_x-1
            
        else:
            # Will also be in infinite while loop
            self.terminator('left')
        
    # This method will mark the block with preset mark   
    def mark_point(self):
        
        # If above block has better heuristic then left block
        if self.H(self.position_x, self.position_y-1) <= self.H(self.position_x-1, self.position_y):
           self.mark_up()
                
        # If left block has better heuristic then above block        
        elif self.H(self.position_x-1, self.position_y) < self.H(self.position_x, self.position_y-1):
           self.mark_left()

        else:
            # If reached then algo has hit dead end and will continue running an empty while loop
            #  which will eventually crash everything ... ask me how I know 
            self.terminator('end')
            
    
    # This method will print out data and terminate the program, In order
    #  to prevent infinite looping          
    def terminator(self,title):
        print(' ')
        print('CURRENT_H: '+ str(self.H(self.position_x, self.position_y)))
        print('POSTION X: '+ str(self.position_x))
        print('POSTION Y: '+ str(self.position_y))
        print('VALUE: '+ str(self.board[self.position_y][self.position_x]))
        print(' ')
        print('ABOVE_H: '+ str(self.H(self.position_x, self.position_y-1)))
        print('POSTION X: '+ str(self.position_x))
        print('POSTION Y-1: '+ str(self.position_y-1))
        print('VALUE: '+ str(self.board[self.position_y-1][self.position_x]))
        print(' ')
        print('LEFT_H: '+ str(self.H(self.position_x-1, self.position_y)))
        print('POSTION X-1: '+ str(self.position_x-1))
        print('POSTION Y: '+ str(self.position_y))
        print('VALUE: '+ str(self.board[self.position_y][self.position_x-1]))
        print(' ')
        print(self.board_cont.print_board(self.board))
        print(' ')
        print('PLACE: '+ str(title))
        print(' ')
        print('TERMINTATING: infinite while loop reached')
        quit()


#test
a_s = A_star()
a_s.path_maker()
