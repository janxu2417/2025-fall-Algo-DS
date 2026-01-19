row = [list(map(int, input().split()))]
mx = [max(row[0])]
mn = row[0]
for i in range(4):
    row.append(list(map(int, input().split())))
    mx.append(max(row[-1]))
    for j in range(5):
        mn[j] = min(mn[j], row[-1][j])
ans = []
for j in range(5):
    for i in range(5):
        if row[i][j] == mn[j] and row[i][j] == mx[i]:
            ans.append((i + 1, j + 1, row[i][j]))
if len(ans):
    print(*ans[0], sep = ' ')
else:
    print('not found')