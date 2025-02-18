# Lesson 11
#get x and y as one input
point = input()
point  = point.split(' ') # splits the string where the whitespace is 10 -11 into ["10", "-11"] becomes a list 

point = list(map(int, point)) #converts strings in the list into integers then list change it into a collection 
x, y = point #variable unpacking, assigns value of list to x and y respectively

if x > 0:
    if y > 0:
        print(f"The point ({x}, {y}) is in Quadrant 1")
    else: 
        print(f"The point ({x}, {y}) is in Quadrant 4")
if x < 0:
    if y > 0:
        print(f"The point ({x}, {y}) is in Quadrant 2")
    else:
        print(f"The point ({x}, {y}) is in Quadrant 3")