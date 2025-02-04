import dataSheet
class rigBuilder:
    def __init__(self, restriction):
        ###Computer is a collection of components
        self.computer = []
        ###restriction is  a set of preset restrictions
        self.restriction = {
            self.money: None, 
            self.ctype: None
        }
        
        dataLists = dataSheet.Datasheet("databaseList.csv")[0]
        for keys in dataLists:
            dataLists[keys] = dataSheet.Datasheet[keys]
            
            

    ###to be employed during the construction of a rigBuilder settings

    ###begin to narrow down the selected; interact with data base, create a culled version
    def applyRestrictions(responseList):
        ###will determine monetary restrictions prior to ranking
        monetaryRestrictionsList = {
            "gaming":[20,40,15,8,9,8],
            "work/general": [30,30,15,8,9,8],
            "powerhouse": [20,45,10,7,10,8]
        }
        
        for restriction in responseList:
            ### if (contains some restrictions):
                ### delete some restriction from the dictionary
        
            
        
    
    ###now dealing with culled data sheet, generate a dictionary of arrays, in which they are in order of priority
    def createPriorityListe():
        ###priorityScheme allows the method of creating a priority to be different
        priorityScheme = 'lowestPrice'
        ##example priority list
        priorityList = {
            "CPU": None,
            "GPU": None,
            "RAM": None,
            "PSU": None,
            "Motherboard": None,
            "Storage": None
        }

        