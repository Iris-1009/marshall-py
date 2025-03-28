# Lesson 44
 
def c_frequency(word):
    #assume word is string
    clean_word = sorted(word.lower())
    answer = {} #empty dict

    for character in clean_word:
        if character not in answer:
            answer[character] = 1
        else:
            answer[character] += 1
    return answer

print(c_frequency("hello"))

