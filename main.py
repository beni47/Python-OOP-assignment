class Person:
  def __init__(self, name, age, gender):
    self.name  = name
    self.age = age
    self.gender = gender
  
  def introduce(self):
    print(f"Hello, my name is {self.name} and I am a {self.age} year old {self.gender} ")

p1 = Person('Ben', 23, 'Male')
p1.introduce()