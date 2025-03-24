# Lesson 31

def anagram(word1, word2):
    if len(word1)!=len(word2):
        return False
    else:
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
        return True

print(anagram("cinema", "iceman"))