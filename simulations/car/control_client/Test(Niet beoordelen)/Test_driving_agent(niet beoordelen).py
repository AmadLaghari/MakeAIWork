'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import time as tm
import traceback as tb
import math as mt
import sys as ss
import os
import socket as sc
import tensorflow as tf
import numpy as np

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters as pm

model_sonar_path = r'C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Sonar/model_sonar'
model_lidar_path = r'C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Lidar/model_lidar'


class DrivingAgent:
    def __init__ (self):
        self.model = None
        self.steeringAngle = 0
        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)
                self.halfApertureAngle = False

                while True:
                    self.input ()
                    self.sweep ()
                    self.output ()
                    self.logTraining ()
                    tm.sleep (0.02)

    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_lidar_path) #lidar uit model path            
        else:
            self.sonarDistances = sensors ['sonarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_sonar_path) #sonar uit model path


    def lidarSweep (self):

        if False:
            nearestObstacleDistance = pm.finity
            nearestObstacleAngle = 0
            
            nextObstacleDistance = pm.finity
            nextObstacleAngle = 0

            for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
                lidarDistance = self.lidarDistances [lidarAngle]
                
                if lidarDistance < nearestObstacleDistance:
                    nextObstacleDistance =  nearestObstacleDistance
                    nextObstacleAngle = nearestObstacleAngle
                    
                    nearestObstacleDistance = lidarDistance 
                    nearestObstacleAngle = lidarAngle

                elif lidarDistance < nextObstacleDistance:
                    nextObstacleDistance = lidarDistance
                    nextObstacleAngle = lidarAngle
            
            targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2 # ik weet de hoek tussen beide pylonnen, en ga daar midden tussendoor rijden

            self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2  # steeringangle wordt bepaald door 2 pionnen
            self.targetVelocity = pm.getTargetVelocity (self.steeringAngle) # bepaald snelheid op basis van de stuurhoek

        sample = [pm.finity for entryIndex in range (pm.lidarInputDim )]
        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])

        steeringangle = self.model.predict(np.array([sample]))
        try:
            self.steeringAngle = float(steeringangle[0][0])
        except:
            self.steeringAngle = float(steeringangle[0])
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)


    def sonarSweep (self):


        steering_angle_model = self.model.predict(np.array([self.sonarDistances]))#steering angle uit model sonar distance ophalen
        self.steeringAngle = float(steering_angle_model[0][0]) # koppelen
        # print(steering_angle_model[0][0])
        
        if False:
            obstacleDistances = [pm.finity for sectorIndex in range (3)]
            obstacleAngles = [0 for sectorIndex in range (3)]
            
            for sectorIndex in (-1, 0, 1):
                sonarDistance = self.sonarDistances [sectorIndex]
                sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
                
                if sonarDistance < obstacleDistances [sectorIndex]:
                    obstacleDistances [sectorIndex] = sonarDistance
                    obstacleAngles [sectorIndex] = sonarAngle

            if obstacleDistances [-1] > obstacleDistances [0]:
                leftIndex = -1
            else:
                leftIndex = 0
            
            if obstacleDistances [1] > obstacleDistances [0]:
                rightIndex = 1
            else:
                rightIndex = 0
            
            self.steeringAngle = (obstacleAngles [leftIndex] + obstacleAngles [rightIndex]) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)

    def logLidarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.lidarInputDim + 1)]

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logSonarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample [entryIndex] = self.sonarDistances [sectorIndex]

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logTraining (self):
        if hasattr (self, 'lidarDistances'):
            self.logLidarTraining ()
        else:
            self.logSonarTraining ()

DrivingAgent ()
