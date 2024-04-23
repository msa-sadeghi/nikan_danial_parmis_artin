class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking")
 
class Beagle(Dog):
    def __init__(self, name, age, gunshy):
        super().__init__(name, age)
        self.gunshy = gunshy
    def hunt(self):
        print(f"{self.name} is hunting")         
dog1 = Dog("jessi", 5)
dog1.bark()
dog2 = Dog("petty", 15)
dog2.bark()
b1 = Beagle("joh", 11, True)
b1.bark()
b1.hunt()