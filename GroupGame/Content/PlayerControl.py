import Zero
import Events
import Keys #Keyboard input
import Property
import VectorMath

#Define Vec3 for easier use
Vec3 = VectorMath.Vec3

class PlayerControl:
    def Initialize(self, initializer):
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, UpdateEvent):
        
        RoomStructure = self.Space.FindObjectByName("LevelSettings")
        PlayerPosition = RoomStructure.LevelStructure.CurrentPlayerPosition
        RoomWidth = RoomStructure.LevelStructure.RoomWidth
        
        
        if (Zero.Keyboard.KeyIsDown(Keys.W) == True): #Move forward if space up is empty
            if (RoomStructure.LevelStructure.RoomArray[PlayerPosition - RoomWidth] == 0):
                #Replace previous space with empty space, and change empty space ahead to 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition - RoomWidth] = 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition] = 0
                
        elif (Zero.Keyboard.KeyIsDown(Keys.S) == True): #Move forward if space up is empty
            if (RoomStructure.LevelStructure.RoomArray[PlayerPosition + RoomWidth] == 0):
                #Replace previous space with empty space, and change empty space ahead to 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition + RoomWidth] = 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition] = 0
                
        elif (Zero.Keyboard.KeyIsDown(Keys.A) == True): #Move forward if space up is empty
            if (RoomStructure.LevelStructure.RoomArray[PlayerPosition - 1] == 0):
                #Replace previous space with empty space, and change empty space ahead to 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition - 1] = 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition] = 0
                
        elif (Zero.Keyboard.KeyIsDown(Keys.D) == True): #Move forward if space up is empty
            if (RoomStructure.LevelStructure.RoomArray[PlayerPosition + 1] == 0):
                #Replace previous space with empty space, and change empty space ahead to 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition + 1] = 76
                RoomStructure.LevelStructure.RoomArray[PlayerPosition] = 0

Zero.RegisterComponent("PlayerControl", PlayerControl)