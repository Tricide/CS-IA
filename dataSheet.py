###switched from openpyxl to pandas
class Datasheet:
    def __init__(self, dataSheet):
        data = []
        with open(dataSheet, "r") as csv_file:
            data = csv_file.read().split("\n")
            
        text = [data[i].split(",") for i in range (len(data))]
        
        for i in range(1, len(text)) :
            data.append({text[0][num]:text[i][num] for num in range(len(text[i]))})
