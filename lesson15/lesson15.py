# Lesson 15

# while loop keeps looping as long as condition is true - used when you dont know when to end
# the condition should get updated in the code block to avoid infinite loop
condition_variable = True
password = "joe"

while condition_variable:
    user_input = input("Enter the password ")
    if user_input == password:
        print("Correct")
        condition_variable = False #ends the loop when correct answer is inputted
    else:
        print("Incorrect")

#for loop looks at each value in a iterable object
user_input = input("Search for a fruit ")
fruits = ['Apple', 'Banana', 'Mango', 'Strawberry']
found = False

for fruit in fruits: 
    if fruit == user_input:
        print("It is found")
        found = True
    
if not found:
    print("It is not found")
