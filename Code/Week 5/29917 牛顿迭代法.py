while True:
    try:
        n = float(input())
        num = 1
        x = 1.0
        y = x - (x ** 2 - n) / (2 * x)
        while abs(y - x) > 10**(-6):
            x, y = y, y - (y ** 2 - n) / (2 * y)
            num += 1
        print(f'{num} {x:.2f}')
    except EOFError:
        break