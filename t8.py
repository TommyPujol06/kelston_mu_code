my_name = input("Name:")
print("Hello, I'm " + my_name + ".  I’m going to help you work out each person’s bill today")

menu = []

count = 0

friend_number = input("how many people are in your group today? ")

friend_number = int(friend_number)

phrase = input("is everyone sharing the bill equally? ")

if phrase == "yes" or phrase == "sure" or phrase == "okay":

  print("Okay. Great!")

how_many = input("how many items did you order? ")

how_many = int(how_many)

for item_number in range(how_many):

  item = input("what‘s  dish " + str(item_number + 1) + "? ")

  menu.append(item)

  total = 0

  total = float(total)

for item in menu:

  cost = input("what’s the cost of " + item + "? > ")

  cost = float(cost)

  total = total + float(cost)

result = total / friend_number

print("Okay, the total cost of the items is $" + str(total))

print("each person has to pay $" + str(result) + " without a tip")

def tip():

  tip_calcu = input("What percentage tip do you want to leave? > ")

  tip_calcu = float(tip_calcu)

  tip = total * (tip_calcu / 100)

  total2 = total + tip

  result2 = total2 / friend_number

  print("A" + str(tip_calcu) + "% tip would be $" + str(tip))

tip()  

print("So, with a tip, everyone has to pay $" + str(result2))

print("Hope you all enjoyed the meal!  😊")