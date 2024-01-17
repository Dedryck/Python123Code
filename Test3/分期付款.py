pricipal = float(input())
months = int(input())
pay_type = input()
months_rate = float(input())

if pay_type == 'ACPI':
    months_pay = pricipal* months_rate(1+months_rate)**months / ((1+ months_rate) ** months -1)
    print(round(months_pay,2))
elif pay_type == 'AC':
    ls = []
    for i in range(1,months + 1):
        months_pay = pricipal / months +(pricipal - pricipal * (i - 1)/ months )* months_rate
        ls.append(round(months_pay,2))
    print(ls)
else:
    print("还款方式输入错误")