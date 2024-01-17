dict1 = {'赵小明': '13299887777', '特明朗': '814666888', '普希京': '522888666', '吴小京': '13999887777'}
ID = input()
IDvalues = input()


if ID in dict1:
    print("您输入的姓名在通讯录中已存在")
else:
    #添加操作
    dict1[ID] = IDvalues
    #遍历字典键对
    for ID,IDvalues in dict1.items():
        print("{}:{}".format(ID,IDvalues))