monthhab = ('pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, '
        'yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu, uayet').split(', ')
tzolkin = ('imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, '
           'chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau').split(', ')
haab = {monthhab[x] : x + 1 for x in range(19)}
def to_tzolkin(x):
    y = max(0, (x - 1) // 260)
    x %= 260
    print(x % 13 if x % 13 else 13, tzolkin[(x + 19) % 20], y, sep = ' ')
    return
m = int(input())
print(m)
for _ in range(m):
    d1, m1, y1 = input().split()
    d = int(d1.rstrip('.')) + 1
    m = haab.get(m1)
    y = int(y1)
    to_tzolkin(d + (m - 1) * 20 + y * 365)