s0 = 'ABCDEFGHIJKL'
n = int(input())
dic = {s0[x] : x for x in range(12)}
def check(i, s):
    ans = 0
    for si in s:
        flag = 0
        if si[2] == 'up':
            if s0[i] in si[0]:
                flag = 1
            elif s0[i] in si[1]:
                flag = -1
        elif si[2] == 'down':
            if s0[i] in si[0]:
                flag = -1
            elif s0[i] in si[1]:
                flag = 1
        if ans and ans == - flag: return 0
        elif flag: ans = flag
    return ans
for _ in range(n):
    flag = [0] * 12
    s = []
    for i in range(3):
        s.append(input().split())
        if s[-1][2] == 'even':
            for j in s[-1][0]:
                flag[dic[j]] = 1
            for j in s[-1][1]:
                flag[dic[j]] = 1
    for i in range(12):
        if not flag[i]:
            c = check(i, s)
            if c:
                print(f'{s0[i]} is the counterfeit coin and it is {"light" if c == -1 else "heavy"}.')
                break