#**********************************************************************************
#PROBLEM WITH THIS CLASS: The pixels encounter an error at run time.
#They try to find the player, but every time the player moves he is destroyed
#Then created again.  Not sure how to fix this with what you have set up right now
#**********************************************************************************
import Zero
import Events
import Property
import VectorMath
import math
import random

Vec3 = VectorMath.Vec3

class PixelLogic:
    
    #Temparary variable used for counting "i"
    Temp = 0
    #Scale and move speed of the Pixels Movement Pattern
    moveSpeed = 0.01
    Scale = 2.5
    #Rotation of the figure 8 cos and sin pattern.
    Rotation = 0
    #Declaring the player variable
    Player = 0
    
    def Initialize(self, initializer):
        #Initializing a random rotation for the pixel
        #Helps keep the pixels all looking different
        self.Rotation = random.randint(0, 180)
        
        #Initializing the player
        self.Player = self.Space.FindObjectByName("ID_76")
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, LogicUpdate):
        #Finding the Time Class
        TimeClass = self.Space.FindObjectByName("LevelSettings")
        TimeClass = TimeClass.LocalTime
        
        #Basing the movement of the pixels off of the game being
        #"Paused" or "Unpaused"
        if(TimeClass.IO):
            self.IdleMove()
        else:
            self.SlowMoMove()
        
    def IdleMove(self):
        #Adding every frame to the temp variable "i++"
        self.Temp += self.moveSpeed
        #Adding every frame to the rotation variable
        self.Rotation += 0.1
        #Define the origin of the pixels movement on the players position
        Origin = self.Player.Transform.Translation
        #Reset the pixels position before calculations
        PixelPosition = Vec3(0,0,0)
        
        #For standard movment of the pixel
        PixelPosition += Vec3(math.cos(self.Temp), math.sin(self.Temp * 2), 0) * self.Scale
        #Now we-
        #Rotate the movement of the sin and cos curves
        #x = xcos(0) - ysin(0)
        #y = xsin(0) + ycos(0)
        PixelPosition.x = PixelPosition.x * math.cos(self.Rotation) - PixelPosition.y * math.sin(self.Rotation)
        PixelPosition.y = PixelPosition.x * math.sin(self.Rotation) + PixelPosition.y * math.cos(self.Rotation)
        PixelPosition += Origin
        
        #Set the final position to the pixel
        self.Owner.Transform.Translation = PixelPosition
        
        def SlowMoMove(self):
            #Adding every frame to the temp variable "i++"
            self.Temp += self.moveSpeed
            #Adding every frame to the rotation variable
            self.Rotation += .001
            #Define the origin of the pixels movement on the players position
            Origin = self.Player.Transform.Translation
            #Reset the pixels position before calculations
            PixelPosition = Vec3(0,0,0)
            
            #For standard movement of pixel
            PixelPosition += Vec3(math.cos(self.Temp), math.sin(self.Temp * 2), 0) * self.Scale
            #Now we-
            #Rotate the movement of the sin and cos curves
            #x = xcos0 - ysin0
            #y = xsin0 + ycos0
            PixelPosition.x = PixelPosition.x*math.cos(self.Rotation) - PixelPosition.y*math.sin(self.Rotation)
            PixelPosition.y = PixelPosition.x*math.sin(self.Rotation) + PixelPosition.y*math.cos(self.Rotation)
            PixelPosition += Origin
            
            #Set the final position to the pixel
            self.Owner.Transform.Translation = PixelPosition

Zero.RegisterComponent("PixelLogic", PixelLogic)