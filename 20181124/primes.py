"""A simple function which will indicate whether a number is a prime or not
"""
def is_prime(n):
    #
    # Check every number up to half of the number
    # we're checking since if we're over half way
    # we must have hit all the factors already
    #
    for factor in range(2, 1 + (n // 2)):
        if n % factor == 0:
            #
            # Bail out as soon as we've found a factor
            #
            return False
    
    #
    # If we haven't found anything, it's a prime
    #
    return True

while True:
    candidate = int(input("Enter a number: "))
    print("Prime" if is_prime(candidate) else "Not Prime")
