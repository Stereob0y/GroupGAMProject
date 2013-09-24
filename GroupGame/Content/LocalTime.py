import Zero
import Events
import Property
import VectorMath

class LocalTime:
    
    IO = True  # On Off Switch
    
    def Initialize(self, initializer):
        self.GlobTimerEvent = Zero.ScriptEvent()
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, UpdateLogic):
        
        
        
        if(self.IO == True):
            
            self.GlobTimerEvent.DT = UpdateLogic.Dt
            self.Space.DispatchEvent("GlobalTimer", self.GlobTimerEvent)
            
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)):
            if(self.IO == True):
                self.IO = False
            elif(self.IO == False):
                self.IO = True
Zero.RegisterComponent("LocalTime", LocalTime)