import dataSheet
class rigBuilder:
    def __init__(self, budget, compType, mType, input):
        ###Computer is a collection of components
        self.computer = []
        ###restriction is  a set of preset restrictions
        ##budget
        self.budget = budget
        
        ##business, powerhouse, gaming
        self.type = compType
       
       
        ##mType determines the algorithm used, powerhouse allows over budget, while cost-effective stays under budget.
        self.mType = mType
        
        
        ##takes inputs from homePage in this order [cpu, gpu, mobo, memory, storage, psu]        
        self.inputList = input
        
        dataLists = dataSheet.Datasheet("databaseList.csv")[0]
        for key in dataLists:
            dataLists[key] = dataSheet.Datasheet(dataLists[key])
            
            
            
    def algorithm(self):
        if self.mType == "powerhouse":
            self.powerAlgorithm()
        if self.mType == "cost-effective":
            self.algorithm2()
            
            
    def powerAlgorithm(self):
        sigma='sigma'
    
    def effectiveAlgorithm(self):
        sigma='sigma'
    
    

    ###begin to narrow down the selected; interact with data base, create a culled version
    def applyRestrictions(self, responseList):
        ###will determine monetary restrictions prior to ranking
        monetaryRestrictionsList = {
            "gaming":[.20,.40,.15,.8,.9,.8],
            "work/general/business": [.30,.30,.15,.8,.9,.8],
            "powerhouse": [.20,.45,.10,.7,.10,.8]
        }
        
        