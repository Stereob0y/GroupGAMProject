import Zero
import Events
import Keys #Keyboard input
import Property
import VectorMath
import math

#Define Vec3 for easier use
Vec3 = VectorMath.Vec3

class PlayerControl:
    
    #PlayerDataArray[0] is always the player's location relative to the level array
    PlayerDataArray = []
    
    AmountofVariables = 4 #Total Variables in the Player (Excluding Position)
    Variable1 = 50 #Mana - Temp
    Variable2 = 100 #Health - Temp
    Variable3 = 25 #Speed
    Variable4 = 0.0 #MoveTimer
    
    def Initialize(self, initializer):
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        AllPlayerPositions = self.PlayerDataArray
        
        #Place other variables in PlayerDataArray; Compatible with multiple players if ever want to implement
        for Players in range(0, len(AllPlayerPositions)):
            
            #Insert (1 "Variable #1" + ("Amount of Variables + 1, because Position is included) multiply by the player's order for the offset)
            self.PlayerDataArray.insert(1 + (self.AmountofVariables + 1 ) * Players, self.Variable1)
            #Do the same for the next variable
            self.PlayerDataArray.insert(2 + (self.AmountofVariables + 1 ) * Players, self.Variable2)
            #Do the same for the next variable
            self.PlayerDataArray.insert(3 + (self.AmountofVariables + 1 ) * Players, self.Variable3)
            #Do the same for the next variable
            self.PlayerDataArray.insert(4 + (self.AmountofVariables + 1 ) * Players, self.Variable4)
            
            
    def OnLogicUpdate(self, UpdateEvent): #every frame
        
        LevelSettings = self.Space.FindObjectByName("LevelSettings")
        RoomWidth = LevelSettings.LevelStructure.RoomWidth
        
        #Go through each player that currently exists
        for PlayerNumber in range(0, round(len(self.PlayerDataArray) / (self.AmountofVariables + 1 ))):
            
            Position = self.PlayerDataArray[0 + (self.AmountofVariables + 1 ) * PlayerNumber]
            LocalVariable1 = self.PlayerDataArray[1 + (self.AmountofVariables + 1 ) * PlayerNumber] #Mana - Temp
            LocalVariable2 = self.PlayerDataArray[2 + (self.AmountofVariables + 1 ) * PlayerNumber] #Health - Temp
            LocalVariable3 = self.PlayerDataArray[3 + (self.AmountofVariables + 1 ) * PlayerNumber] #Speed
            LocalVariable4 = self.PlayerDataArray[4 + (self.AmountofVariables + 1 ) * PlayerNumber] #Move Timer
            
            ChoiceMade = 0 #No choice made
            
            LocalVariable4 += UpdateEvent.Dt
            
            #if the timer passes (10 / Unit Speed) then take a turn
            if (LocalVariable4 > (10 / LocalVariable3)):
                
                #Any type of action that takes up a turn must be on this else if stem
                if (Zero.Keyboard.KeyIsDown(Keys.W) == True): #Move forward if space up is empty
                    if (LevelSettings.LevelStructure.RoomArray[Position - RoomWidth] == 0):
                        #Replace previous space with empty space, and change empty space ahead to 76
                        LevelSettings.LevelStructure.RoomArray[Position - RoomWidth] = 76
                        LevelSettings.LevelStructure.RoomArray[Position] = 0
                        
                        #Update the change to the Position
                        Position = Position - RoomWidth
                        
                        ChoiceMade = 1 #This action counts as the player's choice
                        LocalVariable4 = 0 #Reset the timer, the choice was made
                        
                elif (Zero.Keyboard.KeyIsDown(Keys.S) == True): #Move backward if space up is empty
                    if (LevelSettings.LevelStructure.RoomArray[Position + RoomWidth] == 0):
                        #Replace previous space with empty space, and change empty space behind to 76
                        LevelSettings.LevelStructure.RoomArray[Position + RoomWidth] = 76
                        LevelSettings.LevelStructure.RoomArray[Position] = 0
                        
                        #Update the change to the Position
                        Position = Position + RoomWidth
                        
                        ChoiceMade = 1 #This action counts as the player's choice
                        LocalVariable4 = 0 #Reset the timer, the choice was made
                        
                elif (Zero.Keyboard.KeyIsDown(Keys.A) == True): #Move left if space up is empty
                    if (LevelSettings.LevelStructure.RoomArray[Position - 1] == 0):
                        #Replace previous space with empty space, and change empty space left to 76
                        LevelSettings.LevelStructure.RoomArray[Position - 1] = 76
                        LevelSettings.LevelStructure.RoomArray[Position] = 0
                        
                        #Update the change to the Position
                        Position = Position - 1
                        
                        ChoiceMade = 1 #This action counts as the player's choice
                        LocalVariable4 = 0 #Reset the timer, the choice was made
                        
                elif (Zero.Keyboard.KeyIsDown(Keys.D) == True): #Move right if space up is empty
                    if (LevelSettings.LevelStructure.RoomArray[Position + 1] == 0):
                        #Replace previous space with empty space, and change empty space right to 76
                        LevelSettings.LevelStructure.RoomArray[Position + 1] = 76
                        LevelSettings.LevelStructure.RoomArray[Position] = 0
                        
                        #Update the change to the Position
                        Position = Position + 1
                        
                        ChoiceMade = 1 #This action counts as the player's choice
                        LocalVariable4 = 0 #Reset the timer, the choice was made
                        
            
            #Update the change to the data array
            self.PlayerDataArray[0 + (self.AmountofVariables + 1 ) * PlayerNumber] = Position # Change in Position
            self.PlayerDataArray[1 + (self.AmountofVariables + 1 ) * PlayerNumber] = LocalVariable1 # Change in Mana - Temp
            self.PlayerDataArray[2 + (self.AmountofVariables + 1 ) * PlayerNumber] = LocalVariable2 # Change in Health - Temp
            self.PlayerDataArray[3 + (self.AmountofVariables + 1 ) * PlayerNumber] = LocalVariable3 # Change in Speed
            self.PlayerDataArray[4 + (self.AmountofVariables + 1 ) * PlayerNumber] = LocalVariable4 # Change in Move Timer
            
            #If a choice was made, then commit the choice and update everything else by 1 turn
            if (LevelSettings.LocalTime.IO == False and ChoiceMade == 1):
                LevelSettings.LocalTime.PlayerMove = 1
                

Zero.RegisterComponent("PlayerControl", PlayerControl)