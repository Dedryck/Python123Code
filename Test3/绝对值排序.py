lsit1 = eval(input())
num = sorted(lsit1,key = lambda x: (abs(x),x),reverse = True)
print((',').join(str (x) for x in num))