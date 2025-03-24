# Lesson 30

def createLine(num):
    text = ""
    for i in range(1, num+1):
        if i % 2 == 0:
            text+="0"
        else:
            text+="1"
    return text

def outputPattern(num):
    for i in range(1, num+1):
        print(createLine(i))

print(outputPattern(5))
