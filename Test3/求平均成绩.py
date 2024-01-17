n,m = map(int, input().split())
total_scores = [0] * n
for _ in range(m):
    scores = list(map(float,input().split()))
    for i in range(n):
        total_scores[i] += scores[i]
#算average
for i in total_scores:
    average_scores = i / m
    print("{:.1f}".format(average_scores))

