import dataSheet
class rigBuilder:
    def __init__(self, budget, compType, mType, input):
        ###Computer is a collection of components
        self.computer = ['','','','','','']
        ###restriction is  a set of preset restrictions
        
        self.monetaryRestrictionsList = {
            "gaming":[.20,.40,.15,.8,.9,.8],
            "business": [.30,.30,.15,.8,.9,.8],
            "computing": [.20,.45,.10,.7,.10,.8]
        }
        
        self.dictLists = ["cpuDataBase.csv", "gpuDataBase.csv", "moboDataBase.csv", "memoryDataBase.csv", "storageDataBase.csv", "psuDataBase.csv"]
        
        
        
        
        self.inputList = input
        print(self.inputList)
        
        ##allows use of any list related to components without manipulating them
        ##budget
        self.budget = budget
        print(self.budget)
        
        ##business, powerhouse, gaming
        self.type = compType
        print(self.type)
       
       
        ##mType determines the algorithm used, powerhouse allows over budget, while cost-effective stays under budget.
        self.mType = mType
        print(self.mType)
        
        ##takes inputs from homePage in this order [cpu, gpu, mobo, memory, storage, psu]        
        self.computedRestrictions = [0,0,0,0,0,0]
        self.applyRestrictions()
        print('rigBuilder: restrictions applied')
        print(self.computedRestrictions)
        

            
            
            
    def algorithm(self):
        print('rigBuilder.algorithm: algorithm entered')
        if self.mType == "Power":
            self.powerAlgorithm()
        if self.mType == "Cost-efficiency":
            self.effectiveAlgorithm()
            
            
    def powerAlgorithm(self):
        print('rigbuilder.powerAlgorithm: entered')
        ##search through every remaining dataList
        typeCounter = 0
        for num in self.computedRestrictions:
            if num == 0:
                dataList = dataSheet.Datasheet(self.dictLists[typeCounter]).data
                topChoice = dataList[0]
                
                if self.dictLists[typeCounter] == "cpuDataBase.csv" or self.dictLists[typeCounter]=="gpuDataBase.csv":
                    for item in dataList:
                        if int(topChoice.speed) < int(item.speed) and int(item.price) < self.calcCompBudg(typeCounter):
                            topChoice = item
                
                elif self.dictLists[typeCounter] == "memoryDataBase.csv" or self.dictLists[typeCounter]=="storageDataBase.csv":
                    for item in dataList:
                        if int(topChoice.size) < int(item.size) and int(item.price) < self.calcCompBudg(typeCounter):
                            topChoice = item
                else:
                    for item in dataList:
                        if int(topChoice.price) < int(item.price) and int(item.price) < self.calcCompBudg(typeCounter):
                            topChoice = item
                self.computer[typeCounter] = topChoice
                self.computedRestrictions[typeCounter] = 1

            typeCounter = typeCounter+1
                    
        
    
    def effectiveAlgorithm(self):
        print('rigBuilder.effectiveAlgorithm: entered')
        typeCounter = 0
        for num in self.computedRestrictions:
            if num == 0:
                dataList = dataSheet.Datasheet(self.dictLists[typeCounter]).data
                topChoice = dataList[0]
                
                if self.dictLists[typeCounter] == "cpuDataBase.csv" or self.dictLists[typeCounter]=="gpuDataBase.csv":
                    for item in dataList:
                        if (int(topChoice.speed)/int(topChoice.price)) < (int(item.speed)/int(item.price)) and int(item.price) < self.calcCompBudg(typeCounter) and int(item.price)>self.calcCompBudg(typeCounter)*.7:
                            topChoice = item
                
                elif self.dictLists[typeCounter] == "memoryDataBase.csv" or self.dictLists[typeCounter]=="storageDataBase.csv":
                    for item in dataList:
                        if (int(topChoice.size)/int(topChoice.price)) < (int(item.size)/int(item.price)) and int(item.price) < self.calcCompBudg(typeCounter) and int(item.price)>self.calcCompBudg(typeCounter)*.7:
                            topChoice = item
                else:
                    for item in dataList:
                        if int(topChoice.price) < int(item.price) and int(item.price) < self.calcCompBudg(typeCounter):
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
                for component in dataSheet.Datasheet(self.dictLists[typeCounter]).data:
                    ###find component
                    if component.name == self.inputList[typeCounter]:
                        
                        ###subtract price from overall budget
                        self.budget = self.budget - int(component.price)
                        self.computer[typeCounter] = component
                        
                        self.computedRestrictions[typeCounter] = 1
                        
                        
                
            typeCounter = typeCounter + 1
            
    def calcCompBudg(self, counter):
        temp = []
        for num in self.computedRestrictions:
            for budget in self.monetaryRestrictionsList[self.type]:
                temp.append(num*budget)
        
        return (temp[counter]/sum(temp))*self.budget
        
        
        
                
                
            
        
        
        
        