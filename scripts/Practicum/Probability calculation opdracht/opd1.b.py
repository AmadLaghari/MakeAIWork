import random
import math as m



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
weightX = [1,1,5,1,1,1,1,1,1]
weightO = [1, 0.1, 0.1, 0.1, 0.1, 1,1,1,1,1]







set1 = trainingSet

input = [] 
for ts in set1:
    for laag2 in ts:
        for laag3 in laag2:
            for laag4 in laag3:
                input.append(laag4)
                

print(input)
