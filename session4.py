# numbers = []
# for i in range(4):
#     n = int(input("enter a number: "))
#     numbers.append(n)

# print(numbers)

# ##########################################################

# numbers = []
# i = 0
# while i < 4:
#     n = int(input("enter a number: "))
#     numbers.append(n)
#     i += 1
# print(numbers)



# names = ["nikan", "artin", "danial","amirali"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# for n in names:
#     print(n)


# for i in range(4):
#     print(names[i])

import turtle

my_screen = turtle.Screen()
my_screen.register_shape('strawberry.gif')

my_turtle = turtle.Turtle()
# my_turtle.shape('turtle')
my_turtle.shape('strawberry.gif')
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

for i in range(3):
    my_turtle.forward(130)
    my_turtle.left(120)

for i in range(4):
    my_turtle.forward(130)
    my_turtle.left(90)

turtle.done()