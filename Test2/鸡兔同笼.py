def print_num(a,b):
    rabbits = b/2 - a
    chichen = a - rabbits
    if chichen - int(chichen) != 0 or chichen < 0 or rabbits < 0:
        print("Data Error!")
    else:
        print("有{}只鸡，{}只兔".format(int(chichen),int(rabbits)))
a, b = map(int,input().split())
print_num(a,b)