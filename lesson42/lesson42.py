# Lesson 42

def possible_sum(a_list, target):

    for i, value in enumerate(a_list):
        new_target = target - value
        if new_target in a_list[i+1:]:
            return True
    return False

test = [3, 5, 2, 12, 43]
target = 15

print(possible_sum(test, target))