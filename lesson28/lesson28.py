# Lesson 28

#solution 1 (slicing)
def is_palindrome1(text):
    
    return text == text[::-1] #checks if text is equal to its reversed 

#solution 2 (finds midway point then check to see if the other end is the same)
def is_palindrome2(text):

    if not text:
        return True
    elif len(text) < 4: #for text with length 1,2,3, its a palindrome as long as first and last character are the same
        return text[0] == text[-1]
    else:
        midpoint = len(text)//2
        for i in range(0, midpoint):
            left = text[i]
            right = text[-1*i-1] #if i = 0, -1 if i = 1, -2

            if left != right:
                return False #return in a loop works like a break, ends the loop
        return True

print(is_palindrome1("level"))
print(is_palindrome2("level"))
print(is_palindrome1("apple"))
print(is_palindrome1("apple"))