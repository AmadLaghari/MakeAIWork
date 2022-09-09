import time as tm
from car import Car


class World:
    def __init__(self):
        self.running = True
        self.t = 0.0
        self.dt = 0.1
        self.car = Car('BMW', 500.0, 800)
        self.car2 = Car('Tesla', 800.0, 800)


        

    def bang(self):
        while self.running:
            self.t += self.dt

            self.car.move(self.dt)
            self.car2.move(self.dt)

            if self.car.x > 100:
                self.running = False
                print("BMW heeft gewonnen")

            if self.car2.x > 100:
                self.running = False
                print("Tesla heeft gewonnen")
            
            print("Time: ", self.t)
            tm.sleep(self.dt)
    





            
