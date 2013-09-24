import Zero
import Events
import Keys #Keyboard input
import Property
import VectorMath
import math

#Define Vec3 for easier use
Vec3 = VectorMath.Vec3

class EnemyAI1:
    
    EnemyDataArray = []
    
    AmountofVariables = 2 #Total Variables in this type of AI (Excluding Position)
    Variable1 = 1 #UpDirection
    Variable2 = 100 #Health
    
    def Initialize(self, initializer):
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        AllMonsterPositions = self.EnemyDataArray
        #Place other variables in enemyarraydata
        for Monsters in range(0, len(AllMonsterPositions)):
            
            self.EnemyDataArray.insert(1 + (self.AmountofVariables + 1 ) * Monsters, self.Variable1)
            self.EnemyDataArray.insert(2 + (self.AmountofVariables + 1 ) * Monsters, self.Variable2)
            
        
    def OnLogicUpdate(self, UpdateEvent):
        
        
        RoomStructure = self.Space.FindObjectByName("LevelSettings")
        RoomWidth = RoomStructure.LevelStructure.RoomWidth
        
        #Go through each enemy that currently exists
        for EnemyNumber in range(0, round(len(self.EnemyDataArray) / (self.AmountofVariables + 1 ))):
            
            Position = self.EnemyDataArray[0 + (self.AmountofVariables + 1 ) * EnemyNumber]
            LocalVariable1 = self.EnemyDataArray[1 + (self.AmountofVariables + 1 ) * EnemyNumber]
            LocalVariable2 = self.EnemyDataArray[2 + (self.AmountofVariables + 1 ) * EnemyNumber]
            
            if (RoomStructure.LevelStructure.RoomArray[Position - RoomWidth] == 0 and LocalVariable1 == 1):
                #Replace previous space with empty space, and change empty space ahead to 100
                RoomStructure.LevelStructure.RoomArray[Position - RoomWidth] = 100
                RoomStructure.LevelStructure.RoomArray[Position] = 0
                
                #Update the change to the data array
                self.EnemyDataArray[0 + (self.AmountofVariables + 1 ) * EnemyNumber] = Position - RoomWidth
                
            elif (RoomStructure.LevelStructure.RoomArray[Position - RoomWidth] != 0 and LocalVariable1 == 1):
                self.EnemyDataArray[1 + (self.AmountofVariables + 1 ) * EnemyNumber] = 0 #Change to the down position
                
            elif (RoomStructure.LevelStructure.RoomArray[Position + RoomWidth] == 0 and LocalVariable1 == 0):
                #Replace previous space with empty space, and change empty space behind to 100
                RoomStructure.LevelStructure.RoomArray[Position + RoomWidth] = 100
                RoomStructure.LevelStructure.RoomArray[Position] = 0
                
                #Update the change to the data array
                self.EnemyDataArray[0 + (self.AmountofVariables + 1 ) * EnemyNumber] = Position + RoomWidth
                
            elif (RoomStructure.LevelStructure.RoomArray[Position + RoomWidth] != 0 and LocalVariable1 == 0):
                self.EnemyDataArray[1 + (self.AmountofVariables + 1 ) * EnemyNumber] = 1 #Change to the down position
                
                

Zero.RegisterComponent("EnemyAI1", EnemyAI1)