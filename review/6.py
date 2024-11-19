class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def walk(self):
        print(f"{self.name} is walking")


class Student(Person):
    def __init__(self, n, a, stu_code):
        super().__init__(n, a)
        self.student_code = stu_code
    def learn(self):
        print(f"{self.name} is learning")
        
class Teacher(Person):
    def __init__(self, n, a, exp):
        super().__init__(n, a)
        self.exprience = exp
    def teach(self):
        print(f"{self.name} is teaching")

s1 = Student("blalalal", 14)
t1 = Teacher("BBBBBB", 37)
s1.learn()
t1.teach()