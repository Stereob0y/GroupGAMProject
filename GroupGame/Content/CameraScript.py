import Zero
import Events
import Property
import VectorMath

#Define Vec3 for easier use
Vec3 = VectorMath.Vec3

class CameraScript:
    def Initialize(self, initializer):
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, UpdateEvent):
        
        RoomStructure = self.Space.FindObjectByName("LevelSettings")
        PlayerPosition = RoomStructure.LevelStructure.CurrentPlayerPosition
        RoomWidth = RoomStructure.LevelStructure.RoomWidth
        
        #Focus Camera on player; X position is obtained with Modulus; Y Position is obtained through a truncation of a fraction between Position and Width
        #Also add 1 value because the value starts at 0
        self.Owner.Transform.Translation = Vec3( PlayerPosition % RoomWidth, -(((PlayerPosition - PlayerPosition % RoomWidth) / RoomWidth) + 1) , 5 )

Zero.RegisterComponent("CameraScript", CameraScript)