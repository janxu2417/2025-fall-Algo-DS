def solve():
    n = int(input())
    size = 1 << n
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    inf = float('inf')
    dp = [[inf] * n for _ in range(size)]
    dp[1][0] = 0
    for i in range(1, size, 2):
        for j in range(n):
            if dp[i][j] == inf:
                continue
            for k in range(1, n):
                if (i >> k) & 1:
                    continue
                new_mask = i | (1 << k)
                new_cost = dp[i][j] + cost[j][k]
                if dp[new_mask][k] > new_cost:
                    dp[new_mask][k] = new_cost
    ans = inf
    for i in range(1, n):
        ans = min(ans, dp[size - 1][i] + cost[i][0])
    print(ans)
if __name__ == '__main__':
    solve()