import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            print(num, "is not a prime number ")
            return False
        print(num, "is a prime number")
        return True


print(is_prime(23))
