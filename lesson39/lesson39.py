# Lesson 39

def gcd(num1, num2):

    for divider in range(min(num1, num2), 0, -1):
        if num1 % divider == 0 and num2 % divider == 0:
            return divider #starts from greatest so first divider found will be greatest
    return 1

print(f"the GCD of 8 and 12: {gcd(8, 12)}")

#euclidean algroithm using recursion
def e_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return e_gcd(num2, num1 % num2)

print(f"the GCD of 8 and 12: {e_gcd(8, 12)}")