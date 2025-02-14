# Lesson 4
import math
#input
section1 = input()
section2 = input()
section3 = input()

totalCan = len(section1) + len(section2) + len(section3)
canLeft = totalCan%12
pack = math.ceil(totalCan/12)
price = pack*14.95
print (totalCan)
print (canLeft)
print (price)