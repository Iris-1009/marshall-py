# Lesson 17

num = int(input("Enter a number "))
factorial = 1
for i in range(1, num+1):
    factorial*=i
#end for

print(f"Factorial of {num} is {factorial}")