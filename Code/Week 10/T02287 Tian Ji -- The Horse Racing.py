import sys
import bisect
data = sys.stdin.read().strip().split()
it = iter(data)
def cmp(x, y):
    if x > y: return 400
    if x == y: return 200
    return 0
while True:
    n = int(next(it))
    if not n: break
    a = []
    b = []
    for i in range(n):
        a.append(int(next(it)))
    for i in range(n):
        b.append(int(next(it)))
    a.sort()
    b.sort()
    i = j = 0
    a_to = [-1] * n
    b_to = [-1] * n
    ans = 0
    while i < n:
        while j < n and a[j] <= b[i]:
            j += 1
        if j >= n: break
        a_to[j] = i
        b_to[i] = j
        ans += 400
        i += 1
        j += 1
    # try to regret +1 edge
    if i >= 1:
        j = b_to[i - 1]
        while 1 <= i < n and a[j] > b[i]:
            tmp = 400
            for t in range(1, i + 1):
                tmp = tmp - cmp(a[b_to[i - t]],b[i - t]) + cmp(a[j - t], b[i - t])
                if a_to[j - t] == -1 or tmp <= 0: break
            if tmp <= 0: break
            for t in range(1, i + 1):
                b_to[i - t] = j - t
                if a_to[j - t] == -1:
                    a_to[j - t] = i - t
                    break
                a_to[j - t] = i - t
            a_to[j] = i
            b_to[i] = j
            ans += tmp
            i += 1
        
    if i < n: j = bisect.bisect_left(a, b[i]) 
    while i < n:
        while j < n and (a[j] < b[i] or a_to[j] > 0):
            j += 1
        if j >= n: break
        a_to[j] = i
        b_to[i] = j
        ans += 200
        i += 1
        j += 1
    print(ans - 200 * n)

    
