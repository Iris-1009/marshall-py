# Lesson 37

def str_compress(text):
    result = ''
    ctr = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            ctr += 1
        else:
            result += text[i-1]
            result += str(ctr)
            ctr = 1
    result += text[-1] + str(ctr) #to add the last character

    if len(result) < len(text):
        return result
    else:
        return text
# end of str_compress
    
test = "aabccccaaa"
print(str_compress(test))
