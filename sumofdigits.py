def sum_digits(n):
    return sum(int(num) for num in str(n))


print(sum_digits(12))
