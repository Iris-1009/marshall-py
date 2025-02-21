# Lesson 20
perfect_sum = 0
for num in range (1, 10000):
    factor_sum = 0
    for i in range (1, num):
        if num % i == 0:
            factor_sum+=i
    #end of for inside
    if factor_sum == num: # means perfect number becasue sum of factors(expect itself) equals the number
        perfect_sum+=num
        print(f"{num} is a perfect number")
#end of for outside
print (perfect_sum)