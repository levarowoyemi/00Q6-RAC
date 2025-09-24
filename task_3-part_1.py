class Vehicle:
    def __init__(self, name, max_speed, mileage, colour="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

    def outputVehicle(self):
        return f"Color: {self.colour}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

schoolVolvo = Car("School Volvo", 180, 12)
audiQ5 = Car("Audi Q5", 240, 18)

print(schoolVolvo.outputVehicle())
print(audiQ5.outputVehicle())