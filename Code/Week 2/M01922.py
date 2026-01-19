# greedy
import math
while True:
    n = int(input())
    if not n: break
    a=[]
    for i in range(n):
        vi,ti = map(int,input().split())
        a.append((vi,ti))
    a.sort(key = lambda x : x[0])
    i=0
    v=0
    t0=-1
    for j in range(n):
        if a[j][1] >= 0 and (a[j][1] <= t0 or t0 == -1):
            v,t0 = a[j][0] , a[j][1]
            i = j
    while i < n:
        tmin=-1.0
        opt=-1
        for j in range(i+1,n):
            if a[j][0] == v : continue
            t_meet = (a[j][0]*a[j][1]-v*t0)/(a[j][0]-v)
            if t_meet < 0 : continue
            if tmin < 0 or t_meet <= tmin:
                tmin=t_meet
                opt=j
        if opt == -1 : break
        if v * (tmin - t0) >= 4.5 * 3600 : break
        v = a[opt][0]
        t0 = a[opt][1]
        i = opt
    print(math.ceil(4.5 * 3600 / v + t0))

