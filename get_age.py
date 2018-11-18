import datetime

year = int(input("What year were you born? "))
month = int(input("What month were you born? "))
day = int(input("What day were you born? "))

today = datetime.date.today()
age = today.year - year
if month > today.month:
    age -= 1
elif month == today.month and day > today.day:
    age -= 1

print("You are", age, "years old")