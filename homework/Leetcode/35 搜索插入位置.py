def calc(nums, target):
    li, ri = 0, len(nums) - 1
    while li <= ri:
        mid = (li + ri) // 2
        if nums[mid] == target: return mid
        if nums[mid] < target: li = mid + 1
        else : ri = mid - 1
    return li

nums = list(map(int, input().split()))
target = int(input())
print(calc(nums, target))