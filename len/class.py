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
print("---------------------------------")

class Animal():
  def says(self):
    return "I speak!"

class Horse(Animal):
  def says(self):
    return "Neigh!"
  
class Donkey(Animal):
  def says(self):
    return "Hee-haw"
  
class Mule(Donkey, Horse):
  pass

class Hinny(Horse, Donkey):
  pass

mule = Mule()
hinny = Hinny()

# print(mule.says())
# print(hinny.says())

# Геттеры и сеттеры
class Duck():
  def __init__(self, input_name):
    self.hidden_name = input_name
  def get_name(self):
    print("inside the getter")
    return self.hidden_name
  def set_name(self, input_name):
    print("inside the setter")
    self.hidden_name = input_name
    
# don = Duck("Donald")
# print(don.get_name())

# don.set_name('Donna')
# print(don.get_name())

class Duck():
  def __init__(self, input_name):
    self.hidden_name = input_name
  @property
  def name(self):
    print("inside the getter")
    return self.hidden_name
  @name.setter
  def name(self, input_name):
    print("inside the setter")
    self.hidden_name = input_name
    
fowl = Duck("Howar")
print(fowl.name)

fowl.name = "Doanld"
print(fowl.name)

# Свойства для вычисляемых занчение 
class Circle():
  def __init__(self, radius):
    self.radius = radius
  @property
  def diameter(self):
    return self.radius * 2
  
c = Circle(5)
c.radius
print(c.diameter)
c.radius = 10
print(c.diameter)

#Атрибуты классов и объектов
class Fruit:
  color = 'red'
  
bluberry = Fruit()
print(bluberry.color)
print(Fruit.color)
