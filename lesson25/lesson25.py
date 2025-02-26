# Lesson 25
num = int(input("Enter a number "))
numHolder = num
largest = 0

while num % 2 == 0: #first divides the number by 2 until it is not divisble anymore
    num = num // 2

    largest = max(largest, 2)

if num !=1: #keep checking for factors as long as num is not 1 yet (if its 1, all factors have been found)
    factor = 3
    while num != 1:
        if num % factor == 0:
            num = num // factor
            largest = max(largest, factor)
        else:
            factor+=2 #checks the next odd number

print(f"The largest prime factor for {numHolder} is {largest}")

