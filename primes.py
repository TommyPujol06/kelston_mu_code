def is_prime(n):
    for factor in range(2, 1 + (n // 2)):
        if n % factor == 0:
            return False
    return True

while True:
    candidate = int(input("Enter a number: "))
    print("Prime" if is_prime(candidate) else "Not Prime")
