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
  def exclaim(self):
    print("I'm a Yugo! Much like a Car, but more Yugo-ish")

  def need_a_push(self):
    print("A little help here?")

# print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yogo = Yugo()

give_me_a_car.exclaim()
give_me_a_yogo.exclaim()

give_me_a_yogo.need_a_push()


class Person():
  def __init__(self, name):
    self.name = name
    
class MDPerson(Person):
  def __init__(self, name):
    self.name = "Doctor " + name
    
class JDPerson(Person):
  def __init__(self, name):
    self.name = name + ", Esquire"


person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")


# print(person.name)
# print(doctor.name)
# print(lawyer.name)

class EmailPerson(Person):
  def __init__(self, name, email):
    super().__init__(name)
    self.email = email
    
bob = EmailPerson("BOB", "bob@gmail.com")
print(bob.name, bob.email)




