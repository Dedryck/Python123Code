def fibo(n):
    n1 = 1
    n2 = 1
    n3 = 2
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        
        for i in range(3,n):
            n1 = n2
            n2 = n3
            n3 = n1 + n2
        return n3
n = int(input())
print(fibo(n))