s = input()
stack = [0]
ans = 0
for i in s:
    if i == '(':
        stack.append(0)
    elif i == ')':
        if len(stack) > 1:
            x = stack.pop()
            stack[-1] += x + 2
        else:
            ans = max(ans, stack[0])
            stack[0] = 0
ans = max(ans, max(stack))
print(ans)