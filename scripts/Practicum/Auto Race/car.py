import world
class Car:
    def __init__(self, name, F, m):

        self.name = name
        self.m = m
        self.F = F
        self.v = 0.0
        self.x = 0.0

    def move(self, dt):   
        a = self.F / self.m
        dv = a * dt
        self.v = self.v + dv

        #print("Snelheid: ", self.v)
        print("Snelheid " + self.name + " " + str(self.v))



        dx = self.v * dt
        self.x = self.x + dx

        #print("Afstand: ", self.x)
        print("Afstand " + self.name + " " + str(self.x))


        
    

