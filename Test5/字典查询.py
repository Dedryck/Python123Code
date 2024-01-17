dict1 = {'赵广辉':'13299887777','特朗普':'814666888','普京':'522888666','吴京':'13999887777'}
ID = input()
if ID in dict1:
    print("{}:{}".format(ID,dict1[ID]))
#   print("{}:{}".format(ID,dict1.get(ID)))
else:
    print("数据不存在")