# Lesson 36

def factors(num):
    result = []
    for divider in range(1, num+1):
        if num % divider  == 0:
            result.append(divider)
    return result

def isPrime(num):

    return len(factors(num)) == 2

print(f"factors of 13 is {factors(13)} and is 13 Prime? {isPrime(13)}")


