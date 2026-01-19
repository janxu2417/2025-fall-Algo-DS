n = int(input())
a = list(map(int, input().split()))
num = [0] * 5
for i in a:
    num[i] += 1
ans = num[4] + num[3]
num[1] = max(0, num[1] - num[3])
ans += num[2] // 2
if num[2] % 2:
    ans += 1
    num[1] = max(0, num[1] - 2)
ans += (num[1] + 3) //4
print(ans)