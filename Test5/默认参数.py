def say_hi_default(*info):
    infolist = list(info)
    if len(infolist) == 1:
        return f"尊敬的{infolist[0]}先生，欢迎来到火星！"
    else:
        if infolist[1] == '男':
            infolist[1] = '先生'
        elif infolist[1] == '女':
            infolist[1] = '女士'
        else:
            infolist[1] = '先生/女士'
        return f"尊敬的{infolist[0]}{infolist[1]}，欢迎来到火星！"

            
info = input().split()
print(say_hi_default(*info))

#可变参数在传入以及作为可变参数的时候需要注意*号的添加
#可以用下标来实现对于列表的访问