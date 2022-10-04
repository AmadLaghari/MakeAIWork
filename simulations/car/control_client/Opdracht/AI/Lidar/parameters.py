finity = 20.0   # Needs to be float to obtain ditto numpy array

lidarInputDim = 16
sonarInputDim = 3

sampleFileName = 'sonar_ai.samples'

def getTargetVelocity (steeringAngle):
    return (90 - abs (steeringAngle)) / 60
