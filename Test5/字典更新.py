dict1 = {'赵广辉': '13299887777', '特朗普': '814666888', '普京': '522888666', '吴京': '13999887777'}
ID = input()
Number = input()
if ID not in dict1:
    print("数据不存在")
else:
    dict1[ID] = Number
    
for ID,Number in dict1.items():
    print(f"{ID}:{Number}")
