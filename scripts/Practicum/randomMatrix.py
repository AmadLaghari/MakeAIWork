from tkinter import N
import random
from random import randrange




in_r = random.randint(1,9)
#print(r)

col1 = random.randint(1,4)
rows1 = random.randint(1,4)

m_1 = []

low = 1
high = 10
col = col1
rows = rows1

col_ =  random.randint(1,4)
rows1_ = random.randint(1,4)



standaard_0 = 0

m_1 = [random.choices(range(low,high), k=col_) for _ in range(rows1_)]
lm_1 = len(m_1)
lm_1_= "Aantal Matrix 1 kolom(en) = "
print(lm_1_, lm_1,m_1 )

m_2 = [random.choices(range(low,high), k=col) for _ in range(rows)]
lm_2 = len(m_2)
lm_2_ = "Aantal Matrix 2 Rij(en) = "
print(lm_2_, lm_2, m_2)



m_a = [random.choices(range(low,high), k=lm_1) for _ in range(lm_2)]
m_a_ = "Antwoord index aantal = "
print(m_a_, m_a)


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


matrix_ver(m_1,m_2)

