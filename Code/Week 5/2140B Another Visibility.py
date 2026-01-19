#(a - 1) * y == (10 ** ly - a) * x
# a = x + 1
t = int(input())
#a * (x + y) == x * (10 ** ly) + y
for _ in range(t):
    x = int(input())
    y = 10
    while True:
        if y - x - 1 >= y // 10: break
        y *= 10
    print(y - x - 1)