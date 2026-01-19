s = ''.join([chr(97 + x) for x in range(26)])
dic = {i : (-1, -1) for i in s}
key = (input() + s).replace('j','i')
matrix = [[''] * 5 for _ in range(5)]
x, y = 0, 0
for i in key:
    if dic[i] == (-1, -1):
        matrix[x][y] = i
        dic[i] = (x, y)
        y += 1
        if y == 5:
            x += 1
            y = 0

def encrypt(a, b):
    ax, ay = dic[a][0], dic[a][1]
    bx, by = dic[b][0], dic[b][1]
    if ax == bx:
        return matrix[ax][(ay + 1) % 5] + matrix[bx][(by + 1) % 5]
    if ay == by:
        return matrix[(ax + 1) % 5][ay] + matrix[(bx + 1) % 5][by]
    return matrix[ax][by] + matrix[bx][ay]

for _ in range(int(input())):
    word = input().replace('j','i')
    i = 0
    ans = ''
    while i < len(word):
        if i == len(word) - 1:
            ans = ans + encrypt(word[i], 'x' if word[i] != 'x' else 'q')
        elif word[i] == word[i + 1]:
            ans = ans + encrypt(word[i], 'x' if word[i] != 'x' else 'q')
        else:
            ans = ans + encrypt(word[i], word[i + 1])
            i += 1
        i += 1
    print(ans)