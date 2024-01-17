m = 0
def M(ls):
    global m    
    l=len(ls)
    if m < l:
        m = l
    for i in ls:
        if type(i) == list:
            M(i)
ls = eval(input())
M(ls)
print(m)
