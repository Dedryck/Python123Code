dic = {'admin':'123456','administrator':'12345678','root':'password'}
ID = input()
password = input()
count = 0
while True:
    if ID in dic.keys() and password == dic.get(ID,None) and count <= 2:
        print("登录成功")
        break
    else:
        print("登录失败")
        count +=1
        ID = input()
        password = input()
    
    if count > 2:
        break 