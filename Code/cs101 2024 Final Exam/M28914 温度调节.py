for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b: print(0)
    elif abs(a - b) >= x: print(1)
    elif r - a >= x and r - b >= x or a - l >= x and b - l >= x:
        print(2)
    elif r - a < x and a - l < x or r - b < x and b - l < x:
        print(-1)
    else: print(3)
