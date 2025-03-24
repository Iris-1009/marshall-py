# Lesson 32

def duplicates(word1, word2):
    if not word1 or not word2:
        return [] #returns empty list
    else:
        set_word1 = set(word1)
        set_word2 = set(word2) #set removes duplicates, creates a set of each character in string
        result = []
        for character in set_word1:
            if character in set_word2:
                result.append(character)

        return sorted(result)

print(duplicates("okay", "boat"))

 