n = int(input())

bigmouse = 1
smallmouse = 1
day = 0
time = 1

distencebig, distencesmall = 0,0

while n > 0:
    if n - bigmouse - smallmouse <= 0:
        time = n / (bigmouse + smallmouse)

    #剩余洞长
    n = n - bigmouse - smallmouse
    distencebig =distencebig+ bigmouse*time
    distencesmall = distencesmall+ smallmouse * time
    bigmouse *= 2
    smallmouse *= 0.5
    day = day+ 1
print(day)
print(round(distencesmall,1),round(distencebig,1))
