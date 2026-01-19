for _ in range(int(input())):
    e, f = map(int, input().split())
    m = f - e
    dp = [0] + [1e10] * m
    for i in range(int(input())):
        p, w = map(int, input().split())
        for j in range(m - w + 1):
            dp[j + w] = min(dp[j + w], dp[j] + p)
    if dp[m] == 1e10:
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[m]}.')