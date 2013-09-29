#**********************************************************************************
#PROBLEM WITH THIS CLASS: The pixels encounter an error at run time.
#They try to find the player, but every time the player moves he is destroyed
#Then created again.  Not sure how to fix this with what you have set up right now
#**********************************************************************************
#****************************************
#ATTACH TO EACH PIXEL this class gives
#the pixel all the information it needs
#to have functionality
#****************************************

import Zero
import Events
import Property
import VectorMath
import math
import random

Vec3 = VectorMath.Vec3

class PixelLogic:
    
    #Is assigned a task
    IsChecked = False
    #Is told to go carry out its action or not
    Go = False
    #If Menu is up and not checked
    #then slow mo
    SlowMo = False
    #moveSpeed of the pixel
    moveSpeed = 0
    #Temparary adding var
    Temp = 0
    #Rotation
    Rotation = 0
    #Scale
    Scale = 2
    #Target
    Target = 0
    #Enemy
    Enemy = 0
    
    def Initialize(self, initializer):
        #initializes a random rotation for the pixel
        self.Rotation = random.randint(0, 360)
        #initialize the player variable
        self.Player = self.Space.FindObjectByName("Player")
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, LogicUpdate):
        
        if(self.SlowMo == True):
            #If SlowMo is Set When Menu Is Up
            self.SlowMoMove(LogicUpdate)
        elif(self.IsChecked == True):
            #If IsChecked is Set Run Movment Through Attack()
            self.Attack(LogicUpdate)
        else:
            #If nothing is checked run idle movment
            self.IdleMove(LogicUpdate)
        
    def IdleMove(self, LogicUpdate):
        
        self.Owner.Sprite.Color = VectorMath.Vec4(1,1,1,1)
        
        PixelPosition = Vec3(0, 0, 0)
        self.moveSpeed = 0.07
        self.Temp += self.moveSpeed
        self.Rotation += .01
        Origin = self.Player.Transform.Translation
        
        #For standard movement of pixel
        PixelPosition += Vec3(math.cos(self.Temp), math.sin(self.Temp * 2), 0) * self.Scale
        #Rotated movement of sin and cos curves
        #x = xcos0 - ysin0
        #y = xsin0 + ycos0
        PixelPosition.x = PixelPosition.x*math.cos(self.Rotation) - PixelPosition.y*math.sin(self.Rotation)
        PixelPosition.y = PixelPosition.x*math.sin(self.Rotation) + PixelPosition.y*math.cos(self.Rotation)
        PixelPosition += Origin
        
        self.Owner.Transform.Translation = PixelPosition
        
    def SlowMoMove(self, LogicUpdate):
        #Same function as "IdleMove" but a slower rotation speed
        
        self.moveSpeed = 0.01
        #Adding every frame to the temp variable "x++"
        self.Temp += self.moveSpeed
        self.Rotation += .001
        Origin = self.Player.Transform.Translation
        PixelPosition = Vec3(0,0,0)
        
        #For standard movement of pixel
        PixelPosition += Vec3(math.cos(self.Temp), math.sin(self.Temp * 2), 0) * self.Scale
        #Rotated movement of sin and cos curves
        #x = xcos0 - ysin0
        #y = xsin0 + ycos0
        PixelPosition.x = PixelPosition.x*math.cos(self.Rotation) - PixelPosition.y*math.sin(self.Rotation)
        PixelPosition.y = PixelPosition.x*math.sin(self.Rotation) + PixelPosition.y*math.cos(self.Rotation)
        PixelPosition += Origin
        
        self.Owner.Transform.Translation = PixelPosition
        
    def Attack(self, LogicUpdate):
        #This function runs the update logic for when the pixel is set to attack
        
        PixelPosition = Vec3(0, 0, 0)
        self.moveSpeed = 0.07
        
        #Set the pixel to Go And Carry Out It's Action
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)):
            self.Go = True
        
        if(self.Go == False):
            #STAY IN IDLE MOVMENT UNTIL GO == TRUE
            self.Temp += self.moveSpeed
            self.Rotation += .01
            Origin = self.Player.Transform.Translation
            
            #For standard movement of pixel
            PixelPosition += Vec3(math.cos(self.Temp), math.sin(self.Temp * 2), 0) * self.Scale
            #Rotated movement of sin and cos curves
            #x = xcos0 - ysin0
            #y = xsin0 + ycos0
            PixelPosition.x = PixelPosition.x*math.cos(self.Rotation) - PixelPosition.y*math.sin(self.Rotation)
            PixelPosition.y = PixelPosition.x*math.sin(self.Rotation) + PixelPosition.y*math.cos(self.Rotation)
            PixelPosition += Origin
            
            self.Owner.Transform.Translation = PixelPosition
        else:
            #GO AND ATTACK TARGET WHEN GO == TRUE
            
            #Original Distance from the pixel to the target
            if(self.Target == self.Space.FindObjectByName("Player")):
                OrigDistance = self.Space.FindObjectByName("Player").Transform.Translation - self.Enemy.Transform.Translation
            else:
                OrigDistance = self.Target.Transform.Translation - self.Space.FindObjectByName("Player").Transform.Translation
                self.Enemy = self.Target
            
            OrigDistance = OrigDistance.length()
            
            #Direction for the pixel to follow to the target
            Direction = self.Target.Transform.Translation - self.Owner.Transform.Translation
            #Distance from pixel to target
            Distance = Direction.length()
            Direction.normalize()
            
            #Slow movement when the pixel is close to the player and close to the enemy
            if(Distance < OrigDistance * 0.1 or Distance > OrigDistance * 0.95):
                Speed = 10
            else:
                Speed = 50
            
            self.Owner.Transform.Translation += Direction * Speed * LogicUpdate.Dt
            
            #******************************************************
            #CAUSES BUG WHEN TOO CLOSE TO THE PLAYER, CAN FIX BY 
            #PUTTING LOGIC FOR HEADING BACK TO PLAYER UP IN IDEL
            #******************************************************
            
            #Check to see if the pixels are at the player
            if(self.Target == self.Space.FindObjectByName("Player")):
                if(Distance <= 0.1):
                    self.Go = False
                    self.IsChecked = False
            
            #If the pixels reach the enemy, set the new target to the player
            if(Distance <= 0.9):
                self.Target = self.Space.FindObjectByName("Player")
                
Zero.RegisterComponent("PixelLogic", PixelLogic)