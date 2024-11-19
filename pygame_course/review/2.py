colors = {}
for i in range(3):
    c = input("enter a color: ")
    if c in colors:
        colors[c] += 1
    else:
        colors[c] = 1  
print(colors)
maximum = colors[c]
color = ""
for item in colors.items():
    if item[1] >= maximum:
        maximum = item[1]
        color = item[0]
print(color)
        
    