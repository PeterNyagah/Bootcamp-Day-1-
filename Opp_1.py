class Vehicle(object):


    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
     self.miles = miles
     self.make = make
     self.model = model
     self.year = year
     self.sold_on = sold_on
    def sale_price(self):
      if self.sold_on is not None:
         return 0.0 # Already sold
      else:
         return 5000.0 * self.wheels
    def purchase_price(self):
     if self.sold_on is None:
      return 0.0 # Not yet sold
     else:
      return self.base_sale_price - (.10 * self.miles)

    def vehicle_type(self):
      pass

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4
    def vehicle_type(self):
     return 'car'
class Truck(Vehicle):
    base_sale_price = 10000
    wheels = 8
def vehicle_type(self):
    return 'truck'
class Motorcycle(Vehicle):
    base_sale_price = 4000
    wheels = 2
    def vehicle_type(self):
     return 'motorcycle'
