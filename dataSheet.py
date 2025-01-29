###switched from openpyxl to pandas
import pandas as pd
class Datasheet:
    def __init__(self, dataSheetName):
        self.dataSheetName = dataSheetName
        self.df = pd.read_csv(dataSheetName)

    def applyRestrictions(self, type, data):
        for x in self.df.index:
            if self.df.loc(x, type) == data:
                self.df.drop(x, inplace = True)
        