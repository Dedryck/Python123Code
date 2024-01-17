x,y,z,k=map(int,input().split(" "))
#x为初始基金 ， y为投资时长， z为时长类型 ， k为收益内容

def calculate(x,y,z,k):
    if z==1:
        annual_profit = k
    if z == 2:
        annual_profit = k * 12 / y
    if z == 3 :
        annual_profit = k * 365 / y
    return annual_profit / x
    
rate = calculate(x,y,z,k)

print("在投资金额为:{:.1f},投资时长为{:.1f},收益为:{:.1f}的情况下,年化收益率为:{:.3f}".format(x,y,k,rate))