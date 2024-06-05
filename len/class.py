# class Cat():
#   pass

# a_cat = Cat()
# a_another_cat = Cat()

# a_cat.age = 3
# a_cat.name = "Luci"

# a_cat.nemesis = a_another_cat
# a_cat.nemesis.name = "dodi"


class Cat():
  def __init__(self, name):
    self.name = name
    
furball = Cat('DOD')
# print(furball.name)

class Car():
  def exclaim(self):
    print("I'm Car")

class Yugo(Car):
  pass

# print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yogo = Yugo()

give_me_a_car.exclaim()
give_me_a_yogo.exclaim()


