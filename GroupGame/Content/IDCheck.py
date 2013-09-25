import Zero
import Events
import Property
import VectorMath

class IDCheck:
    MyArrayNumber = 0
    MyID = 0
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
    def OnLogicUpdate(self, UpdateEvent):
        
        RoomStructure = self.Space.FindObjectByName("LevelSettings")
        RoomArray = RoomStructure.LevelStructure.RoomArray
        
        if (RoomArray[self.MyArrayNumber] != self.MyID):
            self.Owner.Destroy()

Zero.RegisterComponent("IDCheck", IDCheck)