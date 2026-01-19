from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i, tmp, ans):
            if s[i:] == s[:i-len(s)-1:-1]:
                ans.append(tmp[:] + [s[i:]])
            for j in range(i + 1, len(s)):
                if s[i:j] == s[j-1:i-len(s)-1:-1]:
                    tmp.append(s[i:j])
                    dfs(j, tmp, ans)
                    tmp.pop()
        ans = []
        dfs(0, [], ans)
        return ans
if __name__ == '__main__':
    s = input()
    solution = Solution()
    res = solution.partition(s)
    print(res)