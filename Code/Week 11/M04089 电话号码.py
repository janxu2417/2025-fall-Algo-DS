class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'
    def insert(self, word : str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = self.end_of_word
    def search(self, word : str) -> bool:
        node = self.root
        for c in word:
            if self.end_of_word in node:
                return True
            if c not in node:
                return False
            node = node[c]

        return True

for _ in range(int(input())):
    n = int(input())
    trie = Trie()
    flag = True
    for i in range(n):
        x = input()
        if trie.search(x): flag = False
        trie.insert(x)
    print('YES' if flag else 'NO')