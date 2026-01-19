from functools import lru_cache

@lru_cache(None)
def check(n, m):
    if n == m:
        return True
    if n % 3 != 0 or n < m:
        return False
    return check(n // 3, m) or check(n * 2 // 3, m)

for _ in range(int(input())):
    n, m = map(int, input().split())
    print('YES' if check(n, m) else 'NO')