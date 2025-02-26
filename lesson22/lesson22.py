# Lesson 22
N = int(input("Enter N to find the Nth Fibonacci Number "))
fib0 = 0
fib1 = 1
fibn = 0

for i in range(2, N+1):
    fibn = fib0+fib1

    fib0 = fib1 #second fib becomes new first fib
    fib1 = fibn #new found fib becomes new second fib

print(f"The Fibonacci Number at {N} is {fibn}")