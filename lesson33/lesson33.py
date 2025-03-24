# Lesson 33

def mean(a_list):
    return sum(a_list) / len(a_list)

def median(a_list):
    sorted_a_list = sorted(a_list)
    middle = len(a_list) // 2
    if len(a_list) % 2 == 0:
        left = sorted_a_list[middle-1]
        right = sorted_a_list[middle]
        return (left+right) / 2
    else:
        return sorted_a_list[middle]

from random import seed
from random import randrange

seed(1)
data = [randrange(1, 100) for _ in range(randrange(10, 30))] #list comprehension
print(f"Dataset: {data}")
print(f"Mean: {mean(data)}")
print(f"Median: {median(data)}")