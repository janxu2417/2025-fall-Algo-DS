import sys

data = sys.stdin.read()
lines = data.splitlines()
i = flag = j = 0
for line in lines:
    list1 = list(map(int, line.split()))
    j = 0
    for x in list1:
        if x == 1:
            flag = 1
            break
        j += 1
    if flag: break
    i += 1
print(abs(i - 2) + abs(j - 2))
