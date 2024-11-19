# a = int(input("enter a number: "))
# b = int(input("enter a number: "))

# print(a  + b)

# name = "parmis"
# family= "sabouri"
# print(f'{name} {family}')

myfile = open("test.txt", "w")
print("artin", "danial", "parmiss", sep="*", end="*", file=myfile)
print("nikan", file=myfile)
import time
message = "hello my friends..."
for c in message:
    print(c, end="", flush=True)
    time.sleep(0.2)