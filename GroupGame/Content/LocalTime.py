import Zero
import Events
import Property
import VectorMath

class LocalTime:
    
    IO = True  # On Off Switch
    
    PlayerMove = 0 # Has player acted this turn; 1 if acted, 0 if not
    
    def Initialize(self, initializer):
        self.GlobTimerEvent = Zero.ScriptEvent()
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, UpdateLogic):
        
        if(self.IO == True):
            
            self.GlobTimerEvent.Dt = UpdateLogic.Dt
            self.Space.DispatchEvent("GlobalTimer", self.GlobTimerEvent)
            
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)):
            if(self.IO == True):
                self.IO = False
            elif(self.IO == False):
                self.IO = True
                
                
        if(self.PlayerMove == 1 and self.IO == True):
            self.IO = False
            self.PlayerMove = 0
            
        if(self.PlayerMove == 1 and self.IO == False):
            self.IO = True
            
Zero.RegisterComponent("LocalTime", LocalTime)