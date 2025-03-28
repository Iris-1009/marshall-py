# Lesson 45

#q1 words to length relationship

def word_length(a_list):
    #assumes only contain strings
    # result = {} #empty dict
    # for word in a_list:
    #     result[word] = len(word)
    # return result 

    #using dictonary comprehension
    return {key : len(key) for key in a_list}


print(word_length(["apple", "banana", "cherry", "date"]))

#q2 fibonacci dictionary 

def d_fib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] = result[i-1] + result[i-2]
        return result
print(d_fib(10))