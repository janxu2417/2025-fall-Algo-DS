from math import log2
q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    nums = [0] * 12
    for i in s:
        if i <= 2048 : nums[int(log2(i))] += 1
    for i in range(11):
        nums[i + 1] += nums[i] // 2
    print('YES' if nums[11] else 'NO')