# Lesson 27

#making a function
def stringCleaner(text):

    result = ''
    for character in text:
        #becuase strings are immutable, you cannot remove the characters directly
        if character.isalpha(): #checks if its an alphabetical character
            result = result + character.lower()
            #.lower makes a string lower case

    return result

value = stringCleaner("Hello0")
print(value)
