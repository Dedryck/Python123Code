dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20} 
dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}
n = int(input())
sort_dic1 = sorted(dic1.keys())
# 取键值的位置
sort_dic2 = sorted(dic2.items(), key=lambda x :x[1])
print(sort_dic1[:n])
print(sort_dic2[:n])