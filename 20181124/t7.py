def is_interesting(n):
    if n % 3 == 0:
        return True
    else:
        return False

for i in range (100):
    number_is_interesting = is_interesting(i)
    if number_is_interesting:
        print "Yes"