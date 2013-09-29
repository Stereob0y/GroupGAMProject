#*******************************************
#ATTACH TO EACH ENEMY, THIS SCRIPT SENDS AN
#EVENT FOR THE MENU TO READ WITH THE ENEMY
#INFORMATION AND SPAWNS THE ENEMY
#*******************************************

import Zero
import Events
import Property
import VectorMath

class IsClicked:
    
    #If the mouse is in the zone
    MouseIn = False
    
    def Initialize(self, initializer):
        
        #Set up the fucntions
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter)
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit)
        
    def OnMouseEnter(self, MouseEvent):
        
        #If mouse enters the enemies box turn the switch to true
        self.MouseIn = True
        
    def OnLogicUpdate(self, LogicEvent):
        
        #Check to see if there are other menues on the screen
        MenuQ = self.Space.FindObjectByName("LevelSettings").MenuManager.IsPlaced
        if(MenuQ == False):
            
            #If mouse is on enemy and input reads right click
            #Then send event with enemies information
            if(self.MouseIn == True):
                
                if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Right)):
                    
                    SpawnMenu = Zero.ScriptEvent()
                    #Sends a location for menu spawning purposes
                    SpawnMenu.Location = self.Owner.Transform.Translation
                    
                    #Sends a target (Cog) for the Pixels to access
                    SpawnMenu.Target = self.Owner
                    
                    self.Space.DispatchEvent("SpawnMenu", SpawnMenu)
                    
                    #Setting the IsPlaced flag to true to signify a menue being active
                    self.Space.FindObjectByName("LevelSettings").MenuManager.IsPlaced = True
                
    def OnMouseExit(self, MouseEvent):
        
        #If mouse exits the enemies box turn the switch to false
        self.MouseIn = False
        
Zero.RegisterComponent("IsClicked", IsClicked)