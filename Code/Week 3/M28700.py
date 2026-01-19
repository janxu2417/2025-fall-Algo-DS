dic={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input()
def rom_to_int():
    ans = 0
    a = []
    for i in s:
        a.append(dic[i])
    n = len(s)
    i = 0
    while i < n:
        if i < n - 1 and a[i] < a[i + 1]:
            ans += a[i + 1] - a[i]
            i += 2
        else:
            ans += a[i]
            i += 1
    print(ans)
    return
def int_to_rom():
    x = int(s)
    ans = ''
    # mod 1000
    if x >= 1000:
        ans += 'M' * (x // 1000)
        x %= 1000
    if x >= 900:
        ans += 'CM'
        x -= 900
    if x >= 500:
        ans += 'D' + 'C' * ((x - 500) // 100)
        x %= 100
    if x >= 400:
        ans += 'CD'
        x -= 400
    if x >= 100:
        ans += 'C' * (x // 100)
        x %= 100
    # <= 100
    if x >= 90:
        ans += 'XC'
        x -= 90
    if x >= 50:
        ans += 'L' + 'X' * ((x - 50) // 10)
        x %= 10
    if x >= 40:
        ans += 'XL'
        x -= 40
    if x >= 10:
        ans += 'X' * (x // 10)
        x %= 10
    # <= 10
    if x >= 9:
        ans += 'IX'
        x -= 9
    if x >= 5:
        ans += 'V' + 'I' * (x - 5)
        x = 0
    if x >= 4:
        ans += 'IV'
        x -= 4
    if x >= 1:
        ans += 'I' * x
    print(ans)
    return
# main
if ord(s[0]) >= ord('A'): rom_to_int()
else: int_to_rom()
