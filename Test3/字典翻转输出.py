or_dic = eval(input())
dic = {}
if (not isinstance (or_dic,dict)):
    print("输入错误")
else:
    for item in or_dic.keys():
        dic[or_dic.get(item)] = item
    print(dic)