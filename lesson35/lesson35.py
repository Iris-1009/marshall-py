# Lesson 35

def remove_duplicates(a_list):
    new_list = []

    for item in a_list:
        if item not in new_list:
            new_list.append(item)

    return new_list 

print(remove_duplicates(['a','b','b','c']))
