from functools import cmp_to_key

def compare(a, b):
    if len(a) != len(b):
        return compare(a + b, b + a)
    mn = len(a)
    for i in range(mn):
        if ord(a[i]) < ord(b[i]):
            return -1
        if ord(a[i]) > ord(b[i]):
            return 1
    return -1
        #return -1   a排在b前面
        #return 1   a排在b后面
n = int(input())
nums = list(input().split())

nums.sort(key=cmp_to_key(compare))
ans=''.join(nums)
ans_=''.join(nums[::-1])
print(ans_,ans,sep=' ')