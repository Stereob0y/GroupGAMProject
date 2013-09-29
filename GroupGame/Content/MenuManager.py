#************************************************************
#Attach to LevelSettings, this scripts soul purpose is to
#listen for the "SpawnMenu" event and spawn the menu + pass 
#the information From the enemy for the attack designation.
#************************************************************

import Zero
import Events
import Property
import VectorMath

class MenuManager:
    
    #Turns true if menu is placed (Set by IsClicked)
    IsPlaced = False
    
    def Initialize(self, initializer):
        
        cameraCog = self.Space.FindObjectByName("Camera")
        Zero.Connect(self.Space, "SpawnMenu", self.GeneratePixelMenu)
        Zero.Connect(cameraCog.Camera.Viewport, Events.MiddleMouseDown, self.ClosePixelMenu)
        
    def GeneratePixelMenu(self, SpawnMenuEvent):
        
        if(self.IsPlaced == False):
            
            #See if there are available pixels
            pixels = [a for a in self.Space.FindAllObjectsByName("Pixel") if not a.PixelLogic.IsChecked]
            
            #if some are available then spawn menu at events posititon
            if(len(pixels) > 0):
                
                SpawnPos = SpawnMenuEvent.Location
                
                SpawnPos.x += 2
                
                SpawnPos.y -= 1.5
                
                self.Space.CreateAtPosition("Menu1", SpawnPos)
                #Send the attack button the target
                Button = self.Space.FindObjectByName("AttackButton")
                Button.GUIPixelAttack.Target = SpawnMenuEvent.Target
                
                #After menu spawns set the pixels that aren't checked to slowmo
                for a in pixels:
                    a.PixelLogic.SlowMo = True
                    
                    
    def ClosePixelMenu(self, ViewportMouseEvent):
        
        if(self.IsPlaced == True):
            object = self.Space.FindObjectByName("Menu1")
            
            self.IsPlaced = False
            object.Destroy()
            
            pixels = [a for a in self.Space.FindAllObjectsByName("Pixel")]
            for a in pixels:
                a.PixelLogic.SlowMo = False

Zero.RegisterComponent("MenuManager", MenuManager)
