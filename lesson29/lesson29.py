# Lesson 29

def consonantCount(text):
    ctr = 0

    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
            ctr+=1
    return ctr

print(consonantCount("hello, world"))