str = input()
g = str.count("G")
l = str.count("L")
d = str.count("D")
flag = 0
if "DDD" in str or l > 1:
    flag = 1

if l<3:
    if flag != 1:
        print("YES")
    else:
        print("No")
else:
    print("No")
#调用内置函数count来数出现的次数