# sports = {}
# while True:
#     name = input("enter a name: ")
#     sport = input("enter a sport: ")
#     # sports[name] = sport
#     sports.update({name : sport})
#     if input("do you want to exit?(y or n): ") == "y":
#         break
    
# print(sports)
# name = input("enter a name: ")    
# # print(f"{name} Likes {sports[name]}")
# print(f"{name} Likes {sports.get(name)}")
  
# d = {}
# for i in range(5):
#     name = input("enter the name: ")
#     score = float(input("enter the score: "))
#     d.update({name:score})
# for key in d:
#     if d[key] > 17:
#         print(key)
    
c = 0   
while True:
    n = int(input("enter a number:> "))
    if n < 0:
        break
    elif n > 15:
        c += 1
print(f"{c} number(s) is(are) greater than 15")
        
    