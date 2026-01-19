# Assignment #B: dp

Updated 1448 GMT+8 Nov 18, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

跳n楼梯的方案数等于跳n-1和n-2楼梯的方案数之和

代码：

```python
n = int(input())
dp = [1, 1]
for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

n的方案数等于0~n-1的方案数之和，也等于n-1方案数两倍，递推可写出通项

代码：

```python
n = int(input())
print(2**(n-1))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M23421:《算法图解》小偷背包问题

dp, http://cs101.openjudge.cn/pctbook/M23421/

思路：

dp[i]表示容量装i可获得最大的价值，则转移方程
dp[j + w[i]] = max(dp[j + w[i]], dp[j] + val[i])
j由大往小遍历，保证一个物品只能选一次。

代码：

```python
n, b = map(int, input().split())
val = list(map(int, input().split()))
w = list(map(int, input().split()))
dp = [0] + [-1] * b
for i in range(n):
    for j in range(b - w[i], -1, -1):
        if dp[j] != -1:
            dp[j + w[i]] = max(dp[j + w[i]], dp[j] + val[i])
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：
dp记录长度为l，初始位置为i的子串是否为回文子串。
dp[l][i] = dp[l-2][i+1] & s[i]==s[i+l-1]
dp[1][i] = 1
dp[2][i] = s[i]==s[i+1]

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[1] * n]
        ans = (0, 0)
        for l in range(2, n + 1):
            dp.append([0] * n)
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] != s[j]: continue
                if l > 2: dp[l - 1][i] = dp[l - 3][i + 1]
                else: dp[l - 1][i] = 1
                if dp[l - 1][i]: ans = (i, j)
        return s[ans[0] : ans[1] + 1]
if __name__ == '__main__':
    s = input()
    print(Solution().longestPalindrome(s))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)






### 474D. Flowers

dp, 1700 https://codeforces.com/problemset/problem/474/D

思路：

花朵数为i的方案数为dp[i]，则转移方程为dp[i]=dp[i-1]+dp[i-k] (i>=k)
利用前缀和快速处理a~b之间的方案数之和

代码：

```python
mod = 1000000007
t, k = map(int, input().split())
dp = [0] * (10 ** 5 + 1)
dp[0] = 1
for i in range(1, 10 ** 5 + 1):
    dp[i] = dp[i - 1]
    if i >= k: dp[i] += dp[i - k]
    dp[i] %= mod
for i in range(1, 10 ** 5 + 1):
    dp[i] = (dp[i] + dp[i - 1]) % mod
for i in range(t):
    a, b = map(int, input().split())
    print((dp[b] - dp[a - 1] + mod) % mod)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)




### M198.打家劫舍

dp, https://leetcode.cn/problems/house-robber/

思路：

y,n分别记录当前位置是否抢的最大收益，则每一个位置i有转移方程
n = max(y,n)
y = n+nums[i]

代码：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        y, n = 0, 0
        for i in nums:
            n, y = max(y, n), n + i
        return max(y, n)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
练习了01742:Coins，拦截导弹，学习了字典树trie




