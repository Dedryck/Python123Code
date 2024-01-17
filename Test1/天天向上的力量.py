x = float(input())

a = 1.0
a *= (1 + x / 100)

b = pow(a,365)

c = pow(1-x/100,365)

print("天天努力的结果{:.3f},天天躺平的结果{:.3f}".format(b,c))