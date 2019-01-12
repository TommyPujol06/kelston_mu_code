import sys
import datetime

year = int(input("What year were you born? "))
month = int(input("What month were you born? "))
day = int(input("What day were you born? "))

yes_no = input("So you were born on %02d/%02d/%04d. Is that correct? [yes/no]" % (day, month, year))
if yes_no.lower() == "no":
    print("Too bad!")
else:
    print("Excellent!")

    today = datetime.date.today()
    age = today.year - year
    if month > today.month:
        age -= 1
    elif month == today.month and day > today.day:
        age -= 1

    print("You are", age, "years old")