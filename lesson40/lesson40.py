# Lesson 40

def factors_list(num):
    result = []
    for divider in range(1, num+1):
        if num % divider == 0:
            result.append(divider)
    return result

def is_prime(num):
    return len(factors_list(num)) == 2
#checks if its a prime number (only 2 factors)

def prime_list(upper_limit):

    primes = [2]
    if upper_limit == 2:
        return primes
    else:
        for num in range(3, upper_limit, 2):
            if is_prime(num):
                primes.append(num)
        return primes

print(f"List of all primes under 10: {prime_list(10)}")
print(f"List of all primes under 10: {prime_list(50)}")