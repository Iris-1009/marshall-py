# Lesson 24

name = ''
longestLength = 0
longestName = ''

while name != 'X':
    name = input("Enter a name or enter 'X' to stop ")
    if name != 'X':
        if len(name) > longestLength:
            longestLength = len(name)
            longestName = name
    else:
        print("Exited")

if longestLength:
    print(f"The longest name is {longestName} with {longestLength} characters")
else:
    print("Not enough information given")