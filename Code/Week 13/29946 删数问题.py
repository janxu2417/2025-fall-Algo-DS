s = input().strip()
k = int(input())
stack = []
num = 0
for i in range(len(s)):
    while stack and int(stack[-1]) > int(s[i]) and num < k:
        stack.pop()
        num += 1
    stack.append(s[i])
while num < k:
    stack.pop()
    num += 1
i = 0
while stack[i] == '0' and i < len(stack) - 1:
    i += 1
print(''.join(stack[i:]))