s = input()
n = len(s)
sum1 = [0] * (n + 1)
for i in range(1, n):
    if s[i] == s[i - 1]:
        sum1[i] = sum1[i - 1] + 1
    else: sum1[i] = sum1[i - 1]
m = int(input())
for _ in range(m):
    li, ri = map(int, input().split())
    print(sum1[ri - 1] - sum1[li - 1])