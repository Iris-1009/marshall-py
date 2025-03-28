# Lesson 41

def scrabble(word):
    total_score = 0
    for character in word:
        current_char = character.upper()
        if current_char in "EAIONRTLSU":
            total_score += 1
        elif current_char in "DG":
            total_score += 2
        elif current_char in "BCMP":
            total_score += 3
        elif current_char in "FHVWY":
            total_score += 4
        elif current_char == "K":
            total_score += 5
        elif current_char in "JX":
            total_score += 8
        elif current_char in "QZ":
            total_score += 10
    return total_score

print(scrabble('graphic'))
    
def best_score(a_list):

    result_list = ["", 0]
    for word in a_list:
        current_score = scrabble(word)

        if current_score > result_list[1]:
            result_list[0] = word
            result_list[1] = current_score

    return result_list

words = ["hello", "bruh"]
print(best_score(words))