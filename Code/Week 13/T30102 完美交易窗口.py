import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    prices = data[1 : n + 1]

    inf = 10**30
    a = [inf]
    a.extend(prices)

    ans = 0
    stack_val = []
    stack_best = []

    push_val = stack_val.append
    push_best = stack_best.append
    pop_val = stack_val.pop
    pop_best = stack_best.pop

    for j in range(n + 1):
        aj = a[j]
        mn = inf
        pos = -1

        while stack_val and stack_val[-1] < aj:
            t = pop_best()
            pop_val()
            at = a[t]
            if at < mn:
                mn = at
                pos = t

        if stack_val:
            t = stack_best[-1]
            at = a[t]
            if at < mn:
                mn = at
                pos = t
            else:
                stack_best[-1] = pos

        push_val(aj)
        push_best(j)

        if pos != -1:
            length = j - pos + 1
            if length > ans:
                ans = length

    sys.stdout.write(str(ans))


if __name__ == '__main__':
    solve()
