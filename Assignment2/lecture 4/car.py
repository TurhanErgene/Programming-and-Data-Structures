class Car:
  def __init__(self, make, model):
    self.__model = model
    self.__make = make

  def set_make(self, make):
    self.__make = make
  
  def get_make(self):
    return self.__make
  
  def set_model(self, model):
    self.__model = model
  
  def get_model(self):
    return self.__model
  
  def __str__(self):
    return f"{self.__make} {self.__model}"
  

  
car1 = Car("Volvo", "XC90")
car2 = Car("Volvo", "V60")
car3 = Car("Volvo", "S90")

car_list = [car1, car2, car3]

print("Original cars:")
for car in car_list:
  print(car)


car2.set_model("XC60")

print("\nAfter modifying the second car:")
for car in car_list:
  print(car)