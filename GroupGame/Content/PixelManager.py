#***************************************
#ATTACH TO THE PLAYER the main purpose
#of this script is to pick a random pixel
#and give it a target and a task.
#***************************************

import Zero
import Events
import Property
import VectorMath
import random
from random import shuffle

class PixelManager:
    
    #Global Variable for number of pixels
    NumPixels = 30
    
    def Initialize(self, initializer):
        
        #Creating Pixels Bassed Of Of NumPixels Variable
        for i in range(0, self.NumPixels):
            self.Space.CreateAtPosition("Pixel", self.Owner.Transform.Translation)
        
        #Connect the function to activate once the attack button has been pressed
        Zero.Connect(self.Space, "ClickedPixelAttack", self.OnAttackClick)
        
    def OnAttackClick(self, Event):
        
        #If GetRand returns something then....
        if(self.GetRandomAvailablePixel()):
            
            #Get Random Pixel
            pixel = self.GetRandomAvailablePixel();
            
            #Set the flag to true
            pixel.PixelLogic.IsChecked = True
            pixel.PixelLogic.SlowMo = False
            #Change the color to green
            pixel.Sprite.Color = VectorMath.Vector4(0, 1, 0, 1)
            
            #Send the pixel its target
            pixel.PixelLogic.Target = Event.Target
            
    def GetRandomAvailablePixel(self):
        
        #Look through all pixels, if the IsChecked == false append it to the array
        pixels = [a for a in self.Space.FindAllObjectsByName("Pixel") if not a.PixelLogic.IsChecked];
        
        #if length = 0, return null to avoid confliction.
        #else return a random pixel from the stack
        if(len(pixels) == 0):
            return None
        else:
            return pixels[ random.randint(0, len(pixels) - 1) ]

Zero.RegisterComponent("PixelManager", PixelManager)