#考点：for循环以及Random模块
import random

def mon(num):
    # a = 0 #循环次数
    count = 0#计数

    for _ in range(times):
        x , y = random.uniform(-1,1),random.uniform(-1,1)
        if x ** 2 + y **2 <=1:
            count +=1
    return 4 * count / times

if __name__ == '__main__':
    sd = int(input())
    random.seed(sd)
    times = int(input())
    print(mon(times))