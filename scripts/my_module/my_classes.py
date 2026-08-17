class Vehicle:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def print(self):
        print(f"Vehicle name: {self.name}, weight: {self.weight}")