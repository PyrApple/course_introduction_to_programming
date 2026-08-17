# %%

# local function
def euro_to_dollar(x, rate=1.16):
    return x * rate

# test function
price = 2
print(f"{price}€ = {euro_to_dollar(price):0.1f}$")

# class vehicle 
class Vehicle:

    # constructor
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    # print vehicle info
    def print(self):
        print(f"Vehicle name: {self.name}, weight: {self.weight}kg")

    # get toll price from weight
    def get_toll_price(self, unit="€"):
        price = self.weight * 0.01
        if( unit == "€"):
            return str(price) + "€"
        else:
            return str(euro_to_dollar(price)) + "$"


# test vehicle class
cars = [Vehicle("Flash", 1300), Vehicle("Martin", 1900)]
for car in cars:
    car.print()
    print(f"toll price for {car.name}: {car.get_toll_price("€")}")
