"""board_controller controller."""

# @Author: Manvir Saini

# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'rumba_controller')))

from controller import Robot
from rumba_controller import Rumba_controller

class Board_controller:

    rt = Rumba_controller()
    
    position_x = 9
    position_y = 9
    mark = 0
    
            #Simulation world 1
            #the Value 1 denotes the end point
            # we use the values -1 or 100 to denote a wall
    # org_board = [[1,0,0,0,0,-1,0,0,0,0],
                 # [0,0,0,0,0,-1,0,0,0,0],
                 # [-1,-1,0,0,0,0,0,0,0,0],
                 # [0,-1,0,0,0,0,0,0,0,0],
                 # [0,0,0,-1,-1,-1,0,0,0,0],
                 # [0,0,0,0,0,0,0,0,-1,-1],
                 # [0,0,0,0,0,0,0,0,0,0],
                 # [0,0,0,0,0,0,-1,0,0,0],
                 # [0,0,0,0,0,0,-1,0,0,0],
                 # [0,0,0,-1,0,0,0,0,0,4]]
             
             #Simulation world 2
    # org_board = [[0,0,0,0,0,-1,0,0,0,0],
                 # [0,0,0,0,0,-1,0,0,0,0],
                 # [1,0,0,0,0,-1,0,0,0,0],
                 # [0,0,0,-1,0,0,0,0,0,0],
                 # [0,0,0,-1,0,0,0,0,0,0],
                 # [0,-1,0,-1,-1,0,-1,-1,0,0],
                 # [0,-1,0,0,0,0,0,0,0,0],
                 # [0,-1,0,-1,0,0,-1,0,-1,-1],
                 # [0,0,0,0,0,0,-1,0,0,0],
                 # [0,0,0,-1,0,0,0,0,0,4]]
                 
             #Simulation world 3
    org_board = [[0,0,0,0,0,-1,0,0,0,0],
                  [0,0,0,0,0,-1,0,0,0,0],
                  [0,0,0,0,0,-1,0,0,0,0],
                  [0,0,0,-1,0,0,0,0,0,0],
                  [0,0,0,-1,0,0,0,0,0,0],
                  [0,-1,0,-1,-1,0,-1,-1,0,0],
                  [0,-1,1,0,0,0,0,0,0,0],
                  [0,-1,0,-1,0,0,-1,0,-1,-1],
                  [0,0,0,0,0,0,-1,0,0,0],
                  [0,0,0,-1,0,0,0,0,0,4]]
                 
    board = org_board
                 
             
    # Just for printing the board 
    def print_board(self, board):
        for r in board:
            for c in r:
                print(c,end =' ')
            print() 
            
            
    # Make robot follow a path outlined 
    #   with a mark on an inputted board
    #
    # Main use function
    def follow_path(self, board, mark):

        self.board = board

        # print('Y POSITION: ' + str(self.position_y))
        self.mark = mark
        
        while self.board[self.position_x][self.position_y] != 1:
            
            direction = 'null'
            
            xPosition = board[self.position_y][self.position_x-1]
            yPosition = board[self.position_y-1][self.position_x]
            
            if xPosition == mark or xPosition == 1:
                direction = 'left'
                
            elif yPosition == mark or yPosition == 1:
                direction = 'up'
            
              
            self.follow_direction(direction, board)
            
        
    # set robot move in a direction 
    def follow_direction(self, direction, board):
        
        if direction == 'left':

            self.left_blocks(board[self.position_y], self.position_x, 0)
            
        elif direction == 'up':

            self.up_blocks(self.position_y, self.position_x, 0)
            
            

    # Move robot for a certain number of blocks
    # recursively find num of blocks to move 
    def left_blocks(self, row, x, numBlocks):
    
        if row[x-1] == self.mark or row[x-1] == 1:
            self.left_blocks(row, x-1, numBlocks+1)
            
        else:
             self.position_x = x 
             self.rt.move_left()
             self.rt.move_forward(numBlocks)
             self.rt.face_north()

        pass
        

    # Move robot for a certain number of blocks
    # recurasivly find num of blocks to move    
    def up_blocks(self, y, x, numBlocks):
        
        if self.board[y-1][x] == self.mark or self.board[y-1][x] == 1:
            self.up_blocks(y-1, x, numBlocks+1)
            
        else:
            self.position_y = y
            self.rt.move_forward(numBlocks)
        
        pass
    


# Testing 


        
            