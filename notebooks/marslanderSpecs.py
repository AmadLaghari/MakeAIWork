import csv

input_dict = { 'length': 6, 'width': 1.56, 'weight': 360, 'deckHeight': (83, 108), 'robotArmLength': 1.8, 'numberOfSolarPanels': 2}
 


csv_columns = ["Attribute", "Value"]
dict_data = [
{"Attribute":"length", "Value": 6},
{"Attribute":'width', "Value": 1.56},
{"Attribute":'weight', "Value": 360}, 
{"Attribute":'deckHeight', "Value": (83, 108)},
{"Attribute":'robotArmLength', "Value": 1.8},
{"Attribute":'numberOfSolarPanels', "Value": 2}
]


csv_file = "marslander.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")