class Vehicle:
    def __init__ (self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
maruti=Vehicle(120,15)
print(maruti.max_speed,maruti.mileage)