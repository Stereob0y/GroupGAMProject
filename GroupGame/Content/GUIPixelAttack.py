#******************************************************************
#ATTACH TO THE PIXEL ATTACK BUTTON OF THE MENU
#the purpose of this script is to add functionality to
#the button and to send the PixelManger the targets information
#******************************************************************

import Zero
import Events
import Property
import VectorMath

Vec4 = VectorMath.Vec4

class GUIPixelAttack:
    
    #Button Colors for the different states
    DefaultColor = Property.Vector4(default = Vec4(0, 1, 0, 1))
    HoverColor = Property.Vector4(default = Vec4(.7, 1, 0, 1))
    DownColor = Property.Vector4(default = Vec4(1, .6, 0, 1))
    
    #Target for attack (Set by "MenuManager")
    Target = 0
    
    def Initialize(self, initializer):
        
        #When menu spawns we check to see if there are any active pixels available
        #If not we keep the button defualt color
        Pixels = self.Space.FindObjectByName("Player").PixelManager.NumPixels
        if(len([a for a in self.Space.FindAllObjectsByName("Pixel") if not a.PixelLogic.IsChecked]) == 0):
           self.DefaultState()
        else:
            Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter)
            Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit)
            Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
            Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown)
            
            self.DefaultState()
        
    ################################################################
    #Behavior
    ################################################################
    def DefaultState(self):
        self.Owner.Sprite.Color = self.DefaultColor
        
    def HoverState(self):
        self.Owner.Sprite.Color = self.HoverColor
        
    def DownState(self):
        self.Owner.Sprite.Color = self.DownColor
        
    ###############################################################
    #Loocal Mouse Events
    ###############################################################
    
    def OnMouseEnter(self, ViewportMouseEvent):
        self.HoverState()
        
    def OnMouseExit(self, ViewportMouseEvent):
        self.DefaultState()
        
    def OnMouseUp(self, ViewportMouseEvent):
        self.HoverState()
        
        #Create a custom script event
        clickedUIButtonEvent = Zero.ScriptEvent()
        #We want to know which object was clicked
        clickedUIButtonEvent.Object = self.Owner
        #Send the targets info to the pixel manager
        clickedUIButtonEvent.Target = self.Target
        #Dispatch the event on the space
        self.Space.DispatchEvent("ClickedPixelAttack", clickedUIButtonEvent)
        
    def OnMouseDown(self, ViewportMouseEvent):
        #The left mouse button was pressed down the object
        #but has not been released yet
        self.DownState()

Zero.RegisterComponent("GUIPixelAttack", GUIPixelAttack)