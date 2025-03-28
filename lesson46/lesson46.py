# Lesson 46

#project euler
def next_value(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (3 * num) + 1

def sequence_maker(start, table):
    if start in table:
        return table[start]
    else:
        sequence = [start] #initialize
        size = 1 

        #while our last value is not one and that we never analyzed the last # before
        while sequence[-1] != 1 and sequence[-1] not in table:
            new_num = next_value(sequence[-1])

            if new_num in table:
                size = size + table[new_num]
                break
            else:
                sequence.append(new_num)
                size+=1

        for i in range(len(sequence)):
            table[sequence[i]] = size - i

        return size 

            #ex. what happens with 13

memory = {1:1, 2:2} 

start = 13
test = sequence_maker(start, memory)

print(f"{start} has {test} many terms")
#to print the sequence
for key, value in memory.items():
    print(f"{key} has {value} many terms")


