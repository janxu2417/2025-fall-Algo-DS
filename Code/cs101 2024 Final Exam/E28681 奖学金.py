n = int(input())
stu = []
for i in range(n):
    a, b, c = map(int, input().split())
    stu.append((-(a + b + c), -a, i + 1))
stu.sort()
for i in range(5):
    print(stu[i][2], -stu[i][0])