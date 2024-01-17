import random
def generate(N):
    return random.randint(pow(10,N-1),pow(10,N)-1)
N = int(input())
random.seed(17)
for i in range(3):
    print(generate(N))
