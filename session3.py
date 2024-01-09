# name = "javascript"
# for x in name:
#     print(x)


# message = "amirali"
# for c in message:
#     print(c)


# a = "game programming"
# print(a[0])
# print(a[15])
# print(a[-1])

# total = 0
# n1 = int(input("Enter a number"))
# n2 = int(input("Enter a number"))
# n3 = int(input("Enter a number"))
# total = n1 + n2 + n3
# print(total)

# total = 0
# for i in range(3):
#     n = int(input("enter a number: "))
#     total += n          # total = total + n
# print(total)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# for n in numbers:
#     print(n)

# students = []
# for i in range(4):
#     name = input("enter a name: ")
#     students.append(name)

# print(students)

# TODO
"""
برنامه ای بنویسید که با کمک حلقه فور
چهار عدد از ورودی دریافت نماید و هر یک از اعداد را درون لیست اضافه کند
در انتها نیز تمامی اعداد موجود در لیست را با هم جمع کنید
"""
my_list = []
for i in range(5):
    name = input("Enter a name: ")
    if len(name) <= 4:
        my_list.append(name)
    else:
        print("blalalall")


print(my_list)
