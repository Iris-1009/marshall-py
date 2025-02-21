# Lesson 13

month = (int)(input())
day = (int)(input())

if month == 2 and day == 18:
    print("Special")
elif month < 2 or (month == 2 and day < 18): #or checks what happens if its in the month so checks the day
    print("Before")
elif month > 2 or (month == 2 and day>18):
    print("After")