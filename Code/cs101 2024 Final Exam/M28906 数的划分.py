from functools import lru_cache
@lru_cache(maxsize = None)
def dfs(n, k, x):
    if k == 1:
        return 1
    ans = 0
    for i in range((n + k - 1) // k, min(n - k + 1, x) + 1):
        ans += dfs(n - i, k - 1, i)
    return ans
#import time
n, k = map(int, input().split())
#start = time.time()
print(dfs(n, k, n))
#print('time taken: ', time.time() - start)