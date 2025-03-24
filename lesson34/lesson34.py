# Lesson 34

def csvToList(text):
    csv = text.split(',')
    a_list = []

    for item in csv:
        a_list.append(int(item))

    return a_list

from random import randrange
def rand_list(start, end, frequency):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            newValue = randrange(start, end+1)
            a_list.append(newValue)
        return a_list
    else:
        return []

print(csvToList("1,2,3,4,5"))
print(rand_list(1, 1000, 30))

     
    