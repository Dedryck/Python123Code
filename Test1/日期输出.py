year = input()
month = input()
date = input()

#考点1，使用sep=""分隔符
print(year,month,date,sep=" ")
print(year,month,date,sep="-")

#考点2，不同拼接符
print(month,date,year,sep=",")

#考点3，拼接字符,也可以使用format函数
print(year + "年" +month+"月"+date+"日")
print("{}年{}月{}日".format(year,month,date))