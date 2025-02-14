# Lesson 3
import math
userInput = int(input())
#input() always a string - int() converts it to an integer
length = math.floor(math.sqrt(userInput))
#square root is just exponent of 1/2 OR math.sqrt
#could also round down to whole num by using floor division //1
print (length)