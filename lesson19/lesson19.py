# Lesson 19

#check the number of factors, if there are two it is a prime number
num = int(input("Enter a number "))
count = 0 #counts how many factors

for i in range (1, num+1):
    if num % i == 0:
        count+=1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")