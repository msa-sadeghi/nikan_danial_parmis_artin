class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking")
        
        
dog1 = Dog("jessi", 5)
dog1.bark()
dog2 = Dog("petty", 15)
dog2.bark()
