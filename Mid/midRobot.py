# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:01:47 2021

@author: aaa
"""

# Assume first and last row is wall and first and last column is wall
TaskEnvModel = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]

# Keep track of cells cleaned by marking cell to 100.  
# Write method to scan table and update self.AllCellsCleaned    
Visited = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]


class Robot:
    
    def __init__(self, x, y):
        # set initial position of robot within task environment.
        self.positionX = x
        self.positionY = y
        self.EnergyConsumed = 0

        # Sensor values.
        self.LeftSensor = 0
        self.RightSensor = 0
        self.FrontSensor = 0
        self.DirtSensor = 0
        
        # Set initial orientation for robot in assigned cell.
        self.Orientation = "North"
        
        # Set goal for robot - All non-wall cells cleaned
        # self.NumberOfCellsToClean = 9     # suboptimal
        # self.NewCellsVisited = 0          # suboptimal
        self.AllCellsCleaned = False
        self.count = 0
        
    # Perceive environment by using virtual robot sensors.
    def Perceive(self):
        
        # Set sensors when robot is facing North
        if self.Orientation == "North":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.FrontSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.BackSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]")
            
        elif self.Orientation == "East":
            self.LeftSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.BackSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]")
            
            #SOUTH
        if self.Orientation == "South":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.FrontSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.BackSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]")
            
            #WEST
        elif self.Orientation == "West":
            self.LeftSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.BackSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]")
            
    def perceiveEnvironment(self):
        
        if self.Orientation == "North":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.FrontSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.BackSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]\n"
                "Enviroment in front of the robot: " + str(self.FrontSensor) + "\n"
                "Enviroment to right of the robot: " + str(self.RightSensor) + "\n"
                "Enviroment to left of the robot: " + str(self.LeftSensor))
            
        elif self.Orientation == "East":
            self.LeftSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.BackSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]\n"
                "Enviroment in front of the robot: " + str(self.FrontSensor) + "\n"
                "Enviroment to right of the robot: " + str(self.RightSensor) + "\n"
                "Enviroment to left of the robot: " + str(self.LeftSensor))
            
            #SOUTH
        if self.Orientation == "South":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.FrontSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.BackSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]\n"
                "Enviroment in front of the robot: " + str(self.FrontSensor) + "\n"
                "Enviroment to right of the robot: " + str(self.RightSensor) + "\n"
                "Enviroment to left of the robot: " + str(self.LeftSensor))
            
            #WEST
        elif self.Orientation == "West":
            self.LeftSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.BackSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]\n"
                "Enviroment in front of the robot: " + str(self.FrontSensor) + "\n"
                "Enviroment to right of the robot: " + str(self.RightSensor) + "\n"
                "Enviroment to left of the robot: " + str(self.LeftSensor))
            
            
    def MoveRobot(self):
        # Navigation strategy go straight first, else turn right, else
        # turn left, else backup when you hit wall
        # Record energy cost.
        
        # if robot orientation is north.
        if self.Orientation == "North":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX - 1
                self.positionY = self.positionY
                self.Orientation == "North"
                print("Robot moved forward to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("Robot Orientation = " + self.Orientation)                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY+1
                self.Orientation = "East"  # new orientation of robot
                print("Robot moved right to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)                
            
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.PositionY - 1
                self.Orientation = "West"
                print("Robot moved left to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)
                
                
                
                
            # ADD CODE:  if front sensor ==1 and right sensor == 1 and 
            # left sensor == 1, move back
 
            
        # if robot orientation is east
        elif self.Orientation == "East":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY + 1
                self.Orientation == "East"
                print("Robot moved forward to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)                
                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX + 1
                self.positionY = self.positionY
                self.Orientation = "South"
                print("Robot moved right to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)      
                
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX - 1 
                self.positionY = self.PositionY
                print("Robot moved Left to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]") 
                self.Orientation = "North"  # New orientation of robot 
                print("New Robot orientation = " + self.Orientation)
                
            
                  
            # ADD CODE: if front sensor ==1 and right sensor == 1 and 
            # left sensor == 1, move back
            
            #if orienntation is West
        elif self.Orientation == "West":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY - 1
                self.Orientation == "West"
                print("Robot moved forward to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)                
                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX - 1
                self.positionY = self.positionY
                self.Orientation = "North"
                print("Robot moved right to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)      
                
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX + 1 
                self.positionY = self.PositionY
                print("Robot moved left to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]") 
                self.Orientation = "South"  # New orientation of robot 
                print("New Robot orientation = " + self.Orientation)
                
            
                
                
    
            # if robot orientation is South.
        elif self.Orientation == "South":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX + 1
                self.positionY = self.positionY
                self.Orientation == "South"
                print("Robot moved forward to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("Robot Orientation = " + self.Orientation)                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY-1
                self.Orientation = "West"  # new orientation of robot
                print("Robot moved right to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)                
            
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.PositionY + 1
                self.Orientation = "East"
                print("Robot moved left to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)
                
                
                
            

    
            
    
        
        
def main():
    
    # Instantiate Robot object.
    robot1 = Robot(1,1)
    
    #while robot1.AllCellsCleaned == False:
    
    # test for two movements
    while robot1.count < 12:
        # Perceive the environment from the robot's initial position.        
       #robot1.Perceive()
        robot1.perceiveEnvironment()
        
        # Move robot to next position.
        robot1.MoveRobot()
        # count robot movements
        robot1.count = robot1.count + 1
        
if __name__ == "__main__":
    main()

        