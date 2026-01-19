class Node:
    def __init__(self, value, idx):
        self.value = value
        self.pre = idx - 1
        self.next = idx + 1

class LinkedList:
    def __init__(self, n):
        self.nodes = []
        #h = list(map(int, input().split()))
        for i in range(n):
            val = int(input())
            self.nodes.append(Node(val, i))
        self.start = 0
        self.tail = n

    def remove(self, idx):
        node = self.nodes[idx]
        if idx == self.start:
            self.start = node.next
        else:
            self.nodes[node.pre].next = node.next
            if node.next == self.tail:
                self.tail = idx
            else:
                self.nodes[node.next].pre = node.pre

    def solve(self, d):
        ans = []
        while self.start != self.tail:
            tmp = []
            i = self.start
            mn = mx = self.nodes[i].value

            while i != self.tail:
                x = self.nodes[i].value
                nxt = self.nodes[i].next
                if mx - d <= x <= mn + d:
                    tmp.append(x)
                    self.remove(i)

                mn = min(mn, x)
                mx = max(mx, x)
                if mx - mn > 2 * d:
                    break
                i = nxt

            ans.extend(sorted(tmp))

        return ans

# main
n, d = map(int, input().split())
q = LinkedList(n)
result = q.solve(d)

print(*result, sep='\n')