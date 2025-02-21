# Lesson 21

N = int(input("Enter a number "))

most = 0
mostFactors = 0

for num in range(1, N+1):
    numFactors = 0
    for i in range(1, num+1):
        if num%i == 0:
            numFactors+=1
    if numFactors > mostFactors:
        most = num #holds the number with the most factors
        mostFactors = numFactors #holds the most number of factors
print(f"{most} has the most factors with {mostFactors} factors")