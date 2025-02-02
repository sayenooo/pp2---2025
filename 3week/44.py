def filter_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return [num for num in a if is_prime(num)]

a = []
while True:
    i = int(input("Enter a number (0 to finish): "))
    a.append(i)
    if i == 0:
        break

prime_numbers = filter_prime(a)
print(prime_numbers)
