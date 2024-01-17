#考点map参数分隔两个数
x,y = map(float,input().split())
def fuli(x,y,z = 40):
    d = x * ((1 + y / 100) ** z)
    print("本金{}元，利率为{:.1f}%的情况下，40年后拥有的资产是{:.3f}元".format(x,y,d))

fuli(x, y)

