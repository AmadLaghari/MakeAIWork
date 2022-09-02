#!/usr/bin/env python3

# digits = list( range(0,100,3) )
# print(sum)
# def averageOfDigits(digits):
#     return (digits/sum(digits))

# averageOfDigits(digits)





# a = list1[0]+list2[0]
# b = list1[1]+list2[1]
# c = list1[2]+list2[2]

# resultaat = [a,b,c]
# print(resultaat)

# def vector(list1, list2):
#     if len(list1) == len(list2):
#         d = list1[0]+list2[0]
#         e = list1[1]+list2[1]
#         f = list1[2]+list2[2]
#         return ([d, e, f])
#     else: return "Broadcasting is niet toegepast"
    

# print(vector(list1, list2))


# Stappen om een Vector-optel calculator te maken
# Benodigheden:
# Checks: 1. Als de lengte van 1 van de vector niet gelijk is aan andere vector. Stap 2 -> Vectors gelijk maken dmv broadcasting
#         2. Als de lengte van beide vectors groter zijn dan 1. Stap 2 -> Nieuwe variable appendden 
#         3. Als de beide vectors gelijk zijn. Stap 2 -> optellen
#         4. Als 1 van de vectors geen of geen geldige waarde bevat. Stap 2 -> User notification Print(Error)


# check 2 > check 1 > check 3 en anders check 4

list1 = [0, 3]
list2 = [1, 6, 9]

print(sum(list1 + list2))

# d = list1[0]+list2[0]
# e = list1[1]+list2[1]


def vector(list1, list2):
    if len(list1) != len(list2):
        if len(list1) <= len(list2):
            verschil_1 = len(list2) - len(list1)
            toevoeging_1 = (verschil_1) * list1.append(0)  # hier moet loop in
            return list1 + list2
        if len(list2) <= len(list1):
            verschil_2 = len(list1) - len(list2)
            toevoeging_2 = verschil_2 * list2.append(0) # hier moet loop in
            return list1 + list2
    elif len(list1) == len(list2):
        return list1 + list2
    elif len(list1) and len(list2) > 1:
        multiplier = len(list1) - 1 
        toevoeging_1_ = multiplier * list1.append([]) # hier moet loop in
        toevoeging_2_ = multiplier * list2.append([]) # hier moet loop in
        return list1 + list2

vector(list1,list2)

#-----------------------------------------------------------------------------
# - functie
# def addVectors(v1, v2):
#     # - start met lege vector
#     resultaat = []

#     # - voor elke rij
#     for: 

#         # - tel de corresponderende elementen bij elkaar op

#         return resultaat
    
#     v1 =list[1,2]
#     v2 = list[2,1]
#     w = addVectors(v1, v2)
