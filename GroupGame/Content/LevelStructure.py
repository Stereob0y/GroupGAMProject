import Zero
import Events
import Property
import VectorMath

#Define Vec3 for easier use
Vec3 = VectorMath.Vec3

class LevelStructure:
    
    RoomID = 0
    CurrentPlayerPosition = 0
    PrevRoomArray = []
    
    #Room Array Format Example
    RoomWidth = 4 #Total Width
    RoomHeight = 4 #Total Height
    RoomArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Exact Layout
    
    def Initialize(self, initializer):
        
        #Based on the RoomID, load the Room's Array Data
        self.LoadRoomArrayData(initializer)
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def LoadRoomArrayData(self, initializer): #See top of page for format example; See Google Docs for ID list
        
        if (self.RoomID == 0): 
            self.RoomWidth = 8 
            self.RoomHeight = 6 
            self.RoomArray = [1,1,1,2,2,1,1,1,1,0,0,0,0,0,0,1,2,0,0,0,0,0,0,2,2,76,0,0,0,0,0,2,1,0,0,0,0,100,0,1,1,1,1,2,2,1,1,1]
            
            
        elif (self.RoomID == 1):
            self.RoomWidth = 2
            self.RoomHeight = 8
            self.RoomArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
        
        for x in range(0, self.RoomWidth * self.RoomHeight): #Resize Previous Array to same size of Current Array with Junk data
            self.PrevRoomArray.append(1000)
        
        #Dump all data that is in the Enemy100Array
        RoomStructure = self.Space.FindObjectByName("LevelSettings")
        RoomStructure.EnemyAI1.EnemyDataArray = []
        
        #Render the Room first without checking for previous arrays since this is the first time rendering
        for IDNum in range(0, (self.RoomWidth * self.RoomHeight)):
            
            #Define the Location to 0,0 when starting a generation
            if (IDNum == 0):
                Locationx = 0
                Locationy = 0
            
            #If the Current Tile is at its end, loop back to x = 0, and decrease its height by 1
            if ((IDNum % self.RoomWidth) == 0):
                Locationx = 0
                Locationy -= 1
            else:
                Locationx += 1
            
            #Get Player Position
            if (self.RoomArray[IDNum] == 76):
                self.CurrentPlayerPosition = IDNum
                
            #Get all enemys with ID 100
            if (self.RoomArray[IDNum] == 100):
                RoomStructure.EnemyAI1.EnemyDataArray.append(IDNum)
                
            IDBlock = self.Space.CreateAtPosition("ID_" + str(self.RoomArray[IDNum]), Vec3( Locationx , Locationy , 1))
            if (IDBlock):
                IDBlock.IDCheck.MyArrayNumber = IDNum
                IDBlock.IDCheck.MyID = self.RoomArray[IDNum]
                
        
    def GenerateLevel(self, UpdateEvent):
        #Reset the Enemy 100 Array before re-rendering
        self.Enemy100Array = []
        
        for IDNum in range(0, (self.RoomWidth * self.RoomHeight)):
            
            #Define the Location to 0,0 when starting a generation
            if (IDNum == 0):
                Locationx = 0
                Locationy = 0
            
            #If the Current Tile is at its end, loop back to x = 0, and decrease its height by 1
            if ((IDNum % self.RoomWidth) == 0):
                Locationx = 0
                Locationy -= 1
            else:
                Locationx += 1
            
            #Get Player Position
            if (self.RoomArray[IDNum] == 76):
                self.CurrentPlayerPosition = IDNum
                
            if (self.RoomArray[IDNum] != self.PrevRoomArray[IDNum]):
                
                self.PrevRoomArray[IDNum] = self.RoomArray[IDNum] #Set the Previous Room Array equal to the new Array
                IDBlock = self.Space.CreateAtPosition("ID_" + str(self.RoomArray[IDNum]), Vec3( Locationx , Locationy , 1))
                if (IDBlock):
                    IDBlock.IDCheck.MyArrayNumber = IDNum
                    IDBlock.IDCheck.MyID = self.RoomArray[IDNum]
                    
        
        
    def OnLogicUpdate(self, UpdateEvent): #Every Game Loop
        #Generate Level on intitializing
        self.GenerateLevel(UpdateEvent)

Zero.RegisterComponent("LevelStructure", LevelStructure)