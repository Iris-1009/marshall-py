# Lesson 38

def is_palindrome(text):
    return text == text[::-1] #check if text is the same backwards

palindromic_numbers = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        current_product = num1 * num2
        if is_palindrome(str(current_product)):
            palindromic_numbers.append(current_product)

print(f"The largest palindromic number is {max(palindromic_numbers)}")

