class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age #protected property

  def get_age(self):     #metode getter untuk mengakses properti privat
    return self.__age

  def set_age(self, age): #metode setter untuk mengubah properti privat
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)   #mengubah umur menjadi 26
print(p1.get_age())

# private methods
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5)  # This would cause an error