#直接倒序找
#倒序遍历更快捷
n = int(input())
for i in range(n,2,-1):
    for k in range(2,i):
        if i % k ==0:
            break
    else:
        print(i)
        break