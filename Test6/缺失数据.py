s = input()
with open('filldata.csv','r',encoding='utf-8') as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    lines[i] = lines[i].split(",")    
    for j in range(len(lines[i])):
        if lines[i][j]=="":
            lines[i][j] = s

print(lines)

#len(lines)返回的是长度，比如lines = ['a','b','c']
#len(lines)=>3