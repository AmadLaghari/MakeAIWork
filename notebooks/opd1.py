import random
import math



#Define Symbols

symbolVecs = {'0': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items ())

# Define datasets (training set should normally be much larger than test set for best results)
# 

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ), '0'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), '0'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ), 'X'),
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ), 'X'),

)



rdrandom = random.uniform(0.1, 1.0)	
rd = round(rdrandom, 1)



set1 = trainingSet[0][0]
# set2 = trainingSet[0][1]
# set3 = trainingSet[0][2]
# set3 = trainingSet[0][3]
m_2 = [1,0]
m_a = []


for rij_index in range(len(set1)):
    print(rij_index)
    for kolom_index in range(len(m_2[0])):
        
         print(kolom_index)









class Node:
    def __init__(self):
        self.value = None
        self.inputLinks = []
    




class Links:
    def __init__(self, inputnode, outputnode, set1):
        self.weight = rd
        self.inputnode = inputnode
        self.outputnode = outputnode
        self.set1 = set1
    
    def link(self):
        for items in set1:
            items.append()
            self.outputnode = self.inputnode * self.weight
            return self.outputnode



def softmax(x):
    e =  math.exp(x)
    return e / e.sum()


def loss():
    return
        


