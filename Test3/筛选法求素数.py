def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return False
    return True
        


def primes_number(n):
    return [i for i in range(2,n) if is_prime(i)]

n = int(input())
print(primes_number(n))