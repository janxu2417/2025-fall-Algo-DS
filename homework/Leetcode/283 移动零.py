nums = list(map(int, input().split()))
i = 0
n = len(nums)
j = 0
while i < n and j < n:
    while i < n and nums[i]: i += 1
    if j <= i: j = i + 1
    while j < n and not nums[j]: j += 1
    while j < n and not nums[i] and nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1
print(*nums,sep=' ')