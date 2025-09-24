# Generic class for all vehicles
class Vehicle:
    # Initializes a Vehicle instance
    def __init__(self, name, max_speed, mileage):
        # The name, maximum speed, and mileage of vehicle
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Returns the seating capacity of the Vehicle
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# A class that represents a Bus, which inherits from the Vehicle class
class Bus(Vehicle):
    # Returns the amount of seats in a vehicle, with a default seating capacity of 50 passengers
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# Instantiates a new Bus object
defaultCapacity = Bus('Honda', 240, 140000)

# Prints out the seating capacity of the new Bus object
print(defaultCapacity.seating_capacity())

