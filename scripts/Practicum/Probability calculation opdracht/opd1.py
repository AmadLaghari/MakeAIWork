import random
import math as m
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
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
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

weightX = [1, 1, 1, 1, 1, 1, 1, 1, 1]
weightO = [1, 1, 1, 1, 1, 1, 1, 1, 1]



# rdrandom = random.uniform(0.1, 1.0)	
# rd = round(rdrandom, 1)






for ts in trainingSet:
    for mainlist in ts:
        for sublist in mainlist:
            for row in sublist:
                pass



set1 = trainingSet[0][0]

input = [] 
for ts in set1:
    for mainlist in ts:
        input.append(mainlist)

print(input)

label = trainingSet[3][1]
for ts_label in label:
    for mainlist_ in ts_label:
        print ("Label: ", mainlist_)

output = []
# for x in input:
#     for y_x in weightX:
#         print(y_x[0])


# for mainlist in trainingSet:
#     for sublist in mainlist[1]:
#         for row in sublist:
#             print (row)

k = [a * b for a,b in zip(input, weightX)]
l = [a * b for a,b in zip(input, weightO)]
print("Label: O ",l, ' ', "Label: X ",k)

sum_k = sum(k)
sum_l = sum(l)

sx_max = m.exp(sum_k)/(m.exp(sum_k)+m.exp(sum_l))
so_max = m.exp(sum_l)/(m.exp(sum_l)+m.exp(sum_k))
# print("Softmax output X: ",sx_max, "Softmax output O: ",so_max)
 
loss = ((1 - 0.88) - (0 - 0.11))**2
# print("Loss ",loss)


def softmax (outputs):
    exponentials = []
    probabilities = []
    for item in outputs:
        exponentials.append(math.exp(item))
    sum_exponentials = sum(exponentials)
    
    for item in exponentials:
        probabilities.append(item/sum_exponentials)
    return probabilities
probablities_ = softmax([9,7])


labels = [1,0]
# Mean Squared Error

def loss (probabilities, labels):
    loss = 0
    if len(probabilities) != len(labels):
        raise "Error"
    for i in range(len(probabilities)):
        error = (labels[i] - probabilities[i])
        sqaured_error = error**2
        loss += sqaured_error
    return loss
    
print(loss(probablities_, labels))




# set2 = trainingSet[0][1]
# set3 = trainingSet[0][2]
# set3 = trainingSet[0][3]
# m_2 = [1,0]
# m_a = []


# for rij_index in range(len(set1)):
#     print(rij_index)
#     for kolom_index in range(len(m_2[0])):
        
#          print(kolom_index)




# class Node:
#     def __init__(self):
#         self.value = None
#         self.inputLinks = []
    




# class Links:
#     def __init__(self, inputnode, outputnode, set1):
#         self.weight = rd
#         self.inputnode = inputnode
#         self.outputnode = outputnode
#         self.set1 = set1
    
#     def link(self):
#         for items in set1:
#             items.append()
#             self.outputnode = self.inputnode * self.weight
#             return self.outputnode



# def softmax(x):
#     e =  math.exp(x)
#     return e / e.sum()


# def loss():
#     return
        


