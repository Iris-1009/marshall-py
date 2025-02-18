# Lesson 10
digits = input("Enter the last four digits of the phone number ")

#if digits[0] == 8 or digits[0] == 9: #checks the first digit, access index of the string using []
#alternative way using in function
if digits[0] in {'8', '9'}:
    if digits[-1] in {'8', '9'}: #-1 gets the last index 
        if digits[1] == digits[2]:
            print("It is a telemarketer")
        else: 
            print("It is not a telemareter")
    else:
        print("It is not a telemarketer") #repeated so that as long as one of the test is not true, returns not a telemarketer
else:
    print("It is not a telemarketer")

