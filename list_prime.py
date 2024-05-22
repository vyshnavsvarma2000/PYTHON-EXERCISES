# WAP to check the prime numbers from a list

def prime(list):
    prime_list = []
    for num in list:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list


print(prime([1, 2, 3, 4, 5]))
