# Lesson 23

Exit = False
totalSum = 0
count = 0

while not Exit:
    mark = input("Enter a number or enter \"Exit\" to stop ")
    if mark == "Exit":
        Exit = True
        break
    else:
        mark = int(mark)
        if mark>=0 and mark<=100:
            totalSum+=mark
            count+=1
        else:
            print("Invalid input")
    
average = totalSum / count
print(f"The average mark is {average}")