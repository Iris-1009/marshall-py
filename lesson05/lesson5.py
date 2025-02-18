# Lesson 5
startMoney = float(input())
cookie = input()

bigCount = int(0)
normalCount = int(0)

for i in range(len(cookie)):
    if cookie[i] == "b":
        bigCount+=1
    elif cookie[i] == "c":
        normalCount+=1

print (f"number of cookies: {bigCount+normalCount}")
cost = (bigCount*0.75) + (normalCount*0.50)
sales = (bigCount*2.00) + (normalCount*1.25)
profit = sales-cost
print (f"profit: ${profit}")
print (f"total amount of money after sales: ${startMoney+profit}")

