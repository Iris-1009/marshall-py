# Lesson 7
from random import randrange

dc = int(input("Enter the DC "))
roll = randrange(1,21) #does not inlcude the second number, ie, does not include 21
print(f"The player has rolled: {roll}")

if roll >= dc:
    print(f"The player was sucessful because {roll} >= {dc}")
else :
    print(f"The player was not sucessful because {roll} < {dc}")


