ls = list(map(int,input().split()))
n = int(input())
filter_list = [x for x in ls if x != n]
if filter_list == ls:
    print("NOT FOUND")
else:
    print(filter_list)