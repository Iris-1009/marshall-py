# Lesson 43

#q1 remove duplicates

def r_duplicates(a_list):
    result = []
    for value in a_list:
        if value not in result:
            result.append(value)
    return result
print(r_duplicates([1,2,2,3,3,4,4,4,]))

#set version
def r_duplicates2(a_list):
    return list(set(a_list))
print(r_duplicates2([1,2,2,3,3,4,4,4,]))

#q2 unique letters in given words

def unique_letters(a_list):
    result_set = set() #use set() not {} b/c thats dict
    for word in a_list:
        tmp_set = set(word) #convert the string word into a set
        result_set = result_set | (tmp_set) #| union operator 
    return result_set

test = ["hello", "goodbye", "world"]
print(unique_letters(test))

#q3 set intersection count
#write a python function that takes a list of sets and returns the count of elements that are common to all sets

def i_count(a_list):
    if a_list:
        result_set = a_list[0] #grabs the first set

        for example_set in a_list[1:]:
            result_set = result_set & example_set #& is the intersection operator
        
        return len(result_set)

test1 = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(i_count(test1))
