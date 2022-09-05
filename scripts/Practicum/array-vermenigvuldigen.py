from tkinter import N
import random
from random import randrange
 



m_1 = [[2,2,2], [4,3,1], [4,7,4]]
m_2 = [[4,4,4], [3,3,3], [3,3,3]]
m_a = [[0,0,0], [0,0,0], [0,0,0]]

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