import time as tm
import traceback as tb
import math as mt
import sys as ss
import os
import socket as sc
import tensorflow as tf
import numpy as np

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 


import parameters as pm


model_lidar_path = r'C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/model_lidar'
model = tf.keras.models.load_model(model_lidar_path)

sample = [pm.finity for entryIndex in range (pm.lidarInputDim)] 
print(sample)
steeringangle = model.predict(np.array([sample][0:16]))

# # print(steeringangle)
# steeringAngle = float(steeringangle[0])
# print(steeringAngle)



sample = [pm.finity for entryIndex in range (pm.sonarInputDim)] 
print(sample)
steeringangle = model.predict(np.array([sample][0:3]))
print(steeringangle)


# model_sonar_path = r'C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/model_sonar'
# model = tf.keras.models.load_model(model_sonar_path)

# sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)] 
# print(sample)
# steeringangle = model.predict(np.array([sample[0:3]]))
# print(model.predict(sample))
# print(steeringangle)
# steeringAngle = float(steeringangle[0][0])
# print(steeringAngle)

# # class Animal:
# #     def __init__(self):
# #         self.num_eyes = 2
    
# #     def breathe(self):
# #         print("inhale and exhale")

# class Fish():
#     def __init__(self):
#         super().__init__()

#     def swim(self):
#         self.s = 7
#         return self.s

#     def ophalen(self):
#         if x == lidar:
#             return self.Distances
#         if s == sonar:
#             return self.Distances
#         return self.Distances


#     def ai(self):
#         self.Distances = Fish().ophalen()
#         self.steeringAngle_modelled = self.model.predict(np.array([self.Distances]))#steering angle uit model sonar distance ophalen
#         self.steeringAngle = float(self.steeringAngle_modelled[0][0]) # koppelen
#         return self.steeringAngle

#     def sonarSweep(self):
       
#         l = Fish().swim()
#         print(6 + l)
#         self.eeeeeeeeeee = 13245

#         print("doing this under water")

# nemo = Fish()
# nemo.sonarSweep()



# class Fruits:
#     def __init__(self,name,clr):
#         self.name = name
#         self.colour = clr
#         self.exp_date = 23

#     def details(self):
#         print(self.exp_date)
#         self.name = 'banana'
#         name = self.name
#         return name

#     def details2(self):
#         self.name = "pineappel"
#         print(self.name)

#     def details3(details.name):
#         print(details.name)


# apple = Fruits("apple", "red")
# apple.details3()


# self.Distances = Distances

# def function:
#     self.steeringAngle_modelled = self.model.predict(np.array([self.Distances]))#steering angle uit model sonar distance ophalen
#     self.steeringAngle = float(self.steeringAngle_modelled[0][0]) # koppelen
