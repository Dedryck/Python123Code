str1 = input()
dic = {}
for i in str1:
    if i in dic:
        dic[i] += 1#计数
    else:
        dic[i] = 1
for i in dic:
    print("字符%s第一次出现在位置：%s,一共出现了%3.3s次"%(i,str1.index(i)),dic[i])