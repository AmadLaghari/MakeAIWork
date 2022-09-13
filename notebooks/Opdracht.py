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
x = 0


class Node:
    def __init__(self):
        self.value = None
        self.inputLinks = []
    
    def node(self):
        for items in self.inputLinks:
            items.append(self.outputnode)



class Links:
    def __init__(self, inputnode, outputnode):
        self.weight = rd
        self.inputnode = inputnode
        self.outputnode = outputnode
    
    def links(self):
        self.outputnode = self.inputnode * self.weight
        return self.outputnode



def softmax(x):
    e =  math.exp(x)
    return e / e.sum()


def loss():
    return
        





m_1 = trainingSet[0][0]
m_a = trainingSet[0][0]
m_2 = trainingSet[0][0]
print(m_1)


def matrix_ver(m_1, m_2):
    if len(m_1) ==  len(range(len(m_2[0]))):
        for rij_index in range(len(m_1)):
            # print(rij_index)
            for kolom_index in range(len(m_2[0])):
                for k in range(len(m_2)):
                    m_a[rij_index][kolom_index] += m_1[rij_index][k] * m_2[k][kolom_index]
        for r in m_a:
            r_antwoord = "Resultaat = "
            print(r_antwoord,r)
    else:
        print("Error: Matrix formaat is niet correct")


