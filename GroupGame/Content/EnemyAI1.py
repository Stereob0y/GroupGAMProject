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
    
    AmountofVariables = 4 #Total Variables in this type of AI (Excluding Position)
    Variable1 = 1 #UpDirection - Temp
    Variable2 = 100 #Health - Temp
    Variable3 = 35 #Speed
    Variable4 = 0.0 #MoveTimer
    
    def Initialize(self, initializer):
        
        Zero.Connect(self.Space, "GlobalTimer" , self.OnGlobalLogicUpdate)
        
        AllMonsterPositions = self.EnemyDataArray
        
        #Place other variables in enemyarraydata
        for Monsters in range(0, len(AllMonsterPositions)):
            
            #Insert (1 "Variable #1" + ("Amount of Variables + 1, because Position is included) multiply by the monster's order for the offset)
            self.EnemyDataArray.insert(1 + (self.AmountofVariables + 1 ) * Monsters, self.Variable1)
            #Do the same for the next variable
            self.EnemyDataArray.insert(2 + (self.AmountofVariables + 1 ) * Monsters, self.Variable2)
            #Do the same for the next variable
            self.EnemyDataArray.insert(3 + (self.AmountofVariables + 1 ) * Monsters, self.Variable3)
            #Do the same for the next variable
            self.EnemyDataArray.insert(4 + (self.AmountofVariables + 1 ) * Monsters, self.Variable4)
            
        
    def OnGlobalLogicUpdate(self, Timer): # need for this to take in the time event
        
        
        LevelSettings = self.Space.FindObjectByName("LevelSettings")
        RoomWidth = LevelSettings.LevelStructure.RoomWidth
        
        #Go through each enemy that currently exists
        for EnemyNumber in range(0, round(len(self.EnemyDataArray) / (self.AmountofVariables + 1 ))):
            
            Position = self.EnemyDataArray[0 + (self.AmountofVariables + 1 ) * EnemyNumber] #Position
            LocalVariable1 = self.EnemyDataArray[1 + (self.AmountofVariables + 1 ) * EnemyNumber] #UpDirection - Temp
            LocalVariable2 = self.EnemyDataArray[2 + (self.AmountofVariables + 1 ) * EnemyNumber] #Health - Temp
            LocalVariable3 = self.EnemyDataArray[3 + (self.AmountofVariables + 1 ) * EnemyNumber] #Speed
            LocalVariable4 = self.EnemyDataArray[4 + (self.AmountofVariables + 1 ) * EnemyNumber] #Move Timer
            
            if (LevelSettings.LocalTime.PlayerMove == 0): #Only Update the Unit's Timer when it is not turn based
                LocalVariable4 += Timer.Dt
                
            #if the timer passes (10 / Unit Speed) then take a turn, or take a turn if the player already took a turn
            if (LocalVariable4 > (10 / LocalVariable3) or LevelSettings.LocalTime.PlayerMove == 1):
                LocalVariable4 = 0 #Reset the timer
                
                if (LevelSettings.LevelStructure.RoomArray[Position - RoomWidth] != 0 and LocalVariable1 == 1):
                    LocalVariable1 = 0 #Change to the down position
                    
                    
                elif (LevelSettings.LevelStructure.RoomArray[Position + RoomWidth] != 0 and LocalVariable1 == 0):
                    LocalVariable1 = 1 #Change to the up position
                    
                    
                if (LevelSettings.LevelStructure.RoomArray[Position - RoomWidth] == 0 and LocalVariable1 == 1):
                    #Replace previous space with empty space, and change empty space ahead to 100
                    LevelSettings.LevelStructure.RoomArray[Position - RoomWidth] = 100
                    LevelSettings.LevelStructure.RoomArray[Position] = 0
                    
                    Position = Position - RoomWidth
                    
                elif (LevelSettings.LevelStructure.RoomArray[Position + RoomWidth] == 0 and LocalVariable1 == 0):
                    #Replace previous space with empty space, and change empty space behind to 100
                    LevelSettings.LevelStructure.RoomArray[Position + RoomWidth] = 100
                    LevelSettings.LevelStructure.RoomArray[Position] = 0
                    
                    Position = Position + RoomWidth
            
            #Update the change to the data array
            self.EnemyDataArray[0 + (self.AmountofVariables + 1 ) * EnemyNumber] = Position
            self.EnemyDataArray[1 + (self.AmountofVariables + 1 ) * EnemyNumber] = LocalVariable1
            self.EnemyDataArray[2 + (self.AmountofVariables + 1 ) * EnemyNumber] = LocalVariable2
            self.EnemyDataArray[3 + (self.AmountofVariables + 1 ) * EnemyNumber] = LocalVariable3
            self.EnemyDataArray[4 + (self.AmountofVariables + 1 ) * EnemyNumber] = LocalVariable4

Zero.RegisterComponent("EnemyAI1", EnemyAI1)