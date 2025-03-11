import dataSheet
class rigBuilder:
    def __init__(self, budget, compType, mType, input):
        ###Computer is a collection of components
        self.computer = []
        ###restriction is  a set of preset restrictions
        
        self.monetaryRestrictionsList = {
            "gaming":[.20,.40,.15,.8,.9,.8],
            "work/general/business": [.30,.30,.15,.8,.9,.8],
            "powerhouse": [.20,.45,.10,.7,.10,.8]
        }
        ##budget
        self.budget = budget
        
        ##business, powerhouse, gaming
        self.type = compType
       
       
        ##mType determines the algorithm used, powerhouse allows over budget, while cost-effective stays under budget.
        self.mType = mType
        
        
        ##takes inputs from homePage in this order [cpu, gpu, mobo, memory, storage, psu]        
        self.inputList = input
        
        self.toFind = self.applyRestrictions()
        
        self.dataLists = dataSheet.Datasheet("databaseList.csv")[0]
        for key in self.dataLists:
            self.dataLists[key] = dataSheet.Datasheet(self.dataLists[key])
            
            
            
    def algorithm(self):
        if self.mType == "powerhouse":
            self.powerAlgorithm()
        if self.mType == "cost-effective":
            self.algorithm2()
            
            
    def powerAlgorithm(self):
        ##search through every remaining dataList
        for item in self.toFind:
            dataList = 
        
    
    def effectiveAlgorithm(self):
        sigma='sigma'
    
    

    ###begin to narrow down the selected; interact with data base, create a culled version
    def applyRestrictions(self):
        ###will determine monetary restrictions prior to ranking
        dictLists = ["cpuDataBase.csv", "gpuDataBase.csv", "moboDataBase.csv", "memoryDataBase.csv", "storageDataBase.csv", "psuDataBase.csv"]
        
        typeCounter = 0
        
        ###Sort through all input
        for response in self.inputList:
            response.strip()
            ###ignore all default choices
            if response != "" and response != None:
                ###sort through all data for the type of input
                for component in dataSheet.Datasheet(dictLists[typeCounter]):
                    ###find component
                    if component.name == self.inputList[typeCounter]:
                        
                        ###subtract price from overall budget
                        self.budget = self.budget - component.price
                        
                        del dictLists[typeCounter]
                        typeCounter = typeCounter - 1
                        
                
            typeCounter = typeCounter + 1
            
        return dictLists
        
                
                
            
        
        
        
        