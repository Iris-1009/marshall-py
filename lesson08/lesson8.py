# Lesson 8
winCount = 0
for i in range(6):
    gameResult = input(f"Enter the result of game {i+1} ")
    if gameResult == "W":
        winCount+=1

group = 0
if winCount >= 5:
    group = 1
elif winCount >= 3:
    group = 2
elif winCount >= 1:
    group = 3

if group == 0:
    print("You are eliminated")
else:
    print(f"You are placed in group {group}")