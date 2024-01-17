with open("info.csv", 'r',encoding='gbk') as f:
    lines = [line.strip().split(',') for line in f]

data_dict = {line[0]:line[1:3] for line in lines}
s = input()
if s == 'A':
    for line in lines:
        print(" ".join(line))
elif s == 'D':
    print(data_dict)
else:
    print("ERROR")