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
        
        self.dictLists = ["cpuDataBase.csv", "gpuDataBase.csv", "moboDataBase.csv", "memoryDataBase.csv", "storageDataBase.csv", "psuDataBase.csv"]
        
        ##allows use of any list related to components without manipulating them
        self.computedRestrictions = [0,0,0,0,0,0]
        ##budget
        self.budget = budget
        
        ##business, powerhouse, gaming
        self.type = compType
       
       
        ##mType determines the algorithm used, powerhouse allows over budget, while cost-effective stays under budget.
        self.mType = mType
        
        
        ##takes inputs from homePage in this order [cpu, gpu, mobo, memory, storage, psu]        
        self.inputList = input
        
        
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
        typeCounter = 0
        for num in self.computedRestrictions:
            if num == 0:
                dataList = dataSheet.Datasheet(self.dictLists[typeCounter]).data
                topChoice = dataList[0]
                
                if self.dictLists[typeCounter] == "cpuDataBase.csv" or self.dictLists[typeCounter]=="gpuDataBase.csv":
                    for item in dataList:
                        if topChoice.speed < item.speed and item.price < self.calCompBudget(typeCounter):
                            topChoice = item
                
                elif self.dictLists[typeCounter] == "memoryDataBase.csv" or self.dictLists[typeCounter]=="storageDataBase.csv":
                    for item in dataList:
                        if topChoice.size < item.size and item.price < self.calCompBudget(typeCounter):
                            topChoice = item
                else:
                    for item in dataList:
                        if topChoice.price < item.price and item.price < self.calCompBudget(typeCounter):
                            topChoice = item
                self.computer[typeCounter] = topChoice
                self.computedRestrictions[typeCounter] = 1
            typeCounter = typeCounter+1
                    
        
    
    def effectiveAlgorithm(self):
        typeCounter = 0
        for num in self.computedRestrictions:
            if num == 0:
                dataList = dataSheet.Datasheet(self.dictLists[typeCounter]).data
                topChoice = dataList[0]
                
                if self.dictLists[typeCounter] == "cpuDataBase.csv" or self.dictLists[typeCounter]=="gpuDataBase.csv":
                    for item in dataList:
                        if (topChoice.speed/topChoice.price) < (item.speed/item.price) and item.price < self.calCompBudget(typeCounter) and item.price>self.calcCompBudg(typeCounter)*.7:
                            topChoice = item
                
                elif self.dictLists[typeCounter] == "memoryDataBase.csv" or self.dictLists[typeCounter]=="storageDataBase.csv":
                    for item in dataList:
                        if (topChoice.size/topChoice.price) < (item.size/item.price) and item.price < self.calCompBudget(typeCounter) and item.price>self.calcCompBudg(typeCounter)*.7:
                            topChoice = item
                else:
                    for item in dataList:
                        if topChoice.price < item.price and item.price < self.calCompBudget(typeCounter):
                            topChoice = item
                self.computer[typeCounter] = topChoice
                self.computedRestrictions[typeCounter] = 1
            typeCounter = typeCounter+1
    
    

    ###begin to narrow down the selected; interact with data base, create a culled version
    def applyRestrictions(self):
        ###will determine monetary restrictions prior to ranking
        
        temp = self.computedRestrictions
        typeCounter = 0
        
        ###Sort through all input
        for response in self.inputList:
            response.strip()
            ###ignore all default choices
            if response != "" and response != None:
                ###sort through all data for the type of input
                for component in dataSheet.Datasheet(self.dictLists[typeCounter]):
                    ###find component
                    if component.name == self.inputList[typeCounter]:
                        
                        ###subtract price from overall budget
                        self.budget = self.budget - component.price
                        
                        self.computedRestrictions[typeCounter] = 1
                        
                        
                
            typeCounter = typeCounter + 1
            
    def calcCompBudg(self, counter):
        temp = []
        for num in self.computedRestrictions:
            for budget in self.monetaryRestrictionsList[self.type]:
                temp.append(num*budget)
        
        return (temp[counter]/sum(temp))*self.budget
        
        
        
                
                
            
        
        
        
        