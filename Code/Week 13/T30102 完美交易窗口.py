import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = [10**30] + data[1 : n + 1]

    ans = 0
    st = []

    st_append = st.append
    st_pop = st.pop
    arr = a

    for j in range(n + 1):
        aj = arr[j]
        mn = 10**30
        pos = -1

        while st and st[-1][1] < aj:
            tmp = st_pop()[2]
            if tmp != -1:
                at = arr[tmp]
                if at < mn:
                    mn = at
                    pos = tmp

        if st:
            top_best = st[-1][2]
            if top_best != -1:
                at = arr[top_best]
                if at < mn:
                    mn = at
                    pos = top_best
                else:
                    st[-1][2] = pos
            else:
                st[-1][2] = pos

        st_append([j, aj, j])

        if pos != -1 and arr[pos] < aj:
            length = j - pos + 1
            if length > ans:
                ans = length

    sys.stdout.write(str(ans))


if __name__ == '__main__':
    solve()
