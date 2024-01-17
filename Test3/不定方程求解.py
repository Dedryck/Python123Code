a, b, c = map(int,input().split())
solutions = []
for x in range(c // a + 1):
    for y in range(c // b +1):
        if a*x + b*y ==c:
            solutions.append([x,y])
print(solutions)
print(len(solutions))