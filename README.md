# Pathfinder

## Project Title

An implementation of A* pathfinding algorithm in WeBots Simulator

## Description

Using 3 simulation worlds to showcase the adaptive nature of the implementation, the algorithm uses a hierarchy set up to change to its given environment. 

High-level we have the A* algorithm itself, comparing heuristics of the next movement to its current location to choose the next best path. 

Mid-level we have the board controller, the A* algo will tell this controller where to move the robot.

Low-level we have the robot controller, which will control the robot movement and speed.



### Dependencies

* WeBots Simluator (https://cyberbotics.com/)

## Authors

@Manvir Saini (https://manvirsaini.github.io/)
