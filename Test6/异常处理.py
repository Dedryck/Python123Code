try:
    #注意一下
    num = eval(input())
    str = '零一二三四五六七八九'
    print(str[num])
except IndexError:
    print("请输入0~9之间的数")
except TypeError:
    print("请输入整数")
except NameError:
    print("请输入整数")
