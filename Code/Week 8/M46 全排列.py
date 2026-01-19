from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, n, flag, tmp, nums, ans):
            if i == n:
                ans.append(tmp[:])
                return
            for j in range(n):
                if not flag[j]:
                    flag[j] = 1
                    tmp.append(nums[j])
                    dfs(i + 1, n, flag, tmp, nums, ans)
                    flag[j] = 0
                    tmp.pop()
        n = len(nums)
        flag = [0] * n
        tmp = []
        ans = []
        dfs(0, n, flag, tmp, nums, ans)
        return ans
if __name__ == '__main__':
    nums = list(map(int, input().split()))
    solution = Solution()
    res = solution.permute(nums)
    print(res)