# Assignment #3: 语法练习

Updated 1440 GMT+8 Sep 29, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/pctbook/E28674/



思路：
将字符转化成a~z当中的排序值（通过ASCII码实现），在mod 26意义下减k


代码

```python
k = int(input())
s = input()
k %= 26
for i in s:
    if ord(i) >= ord('a'):
        print(chr(ord('a') + (ord(i) - ord('a') - k + 26) % 26), end='')
    else:
        print(chr(ord('A') + (ord(i) - ord('A') - k + 26) % 26), end='')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/pctbook/E28691/



思路：
split()函数的使用


代码

```python
a, b = input().split()
print(int(a[:2]) + int(b[:2]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M28664: 验证身份证号 

http://cs101.openjudge.cn/pctbook/M28664/



思路：

按照题意实现

代码

```python
a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

yushu='1,0,X,9,8,7,6,5,4,3,2'.split(',')

n = int(input())
for i in range(n):
    s = input()
    num = 0
    for j in range(17):
        num += a[j] * int(s[j])
    num %= 11
    print('YES' if s[-1] == yushu[num] else 'NO')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M28678: 角谷猜想

http://cs101.openjudge.cn/pctbook/M28678/


思路：

循环实现

代码

```python
n = int(input())
while n > 1:
    if n % 2:
        print(n,'*3+1=',n * 3 + 1, sep='')
        n = n * 3 + 1
    else:
        print(n,'/2=',n//2,sep='')
        n //= 2
print('End')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/pctbook/M28700/



思路：

罗马转数字时，注意4和9的特例都是小的在大的前面，将这一条件加入判断即可。
在1000、100、10、1位上逐一处理，对4和9的特例用if判断

代码

```python
dic={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input()
def rom_to_int():
    ans = 0
    a = []
    for i in s:
        a.append(dic[i])
    n = len(s)
    i = 0
    while i < n:
        if i < n - 1 and a[i] < a[i + 1]:
            ans += a[i + 1] - a[i]
            i += 2
        else:
            ans += a[i]
            i += 1
    print(ans)
    return
def int_to_rom():
    x = int(s)
    ans = ''
    # mod 1000
    if x >= 1000:
        ans += 'M' * (x // 1000)
        x %= 1000
    if x >= 900:
        ans += 'CM'
        x -= 900
    if x >= 500:
        ans += 'D' + 'C' * ((x - 500) // 100)
        x %= 100
    if x >= 400:
        ans += 'CD'
        x -= 400
    if x >= 100:
        ans += 'C' * (x // 100)
        x %= 100
    # <= 100
    if x >= 90:
        ans += 'XC'
        x -= 90
    if x >= 50:
        ans += 'L' + 'X' * ((x - 50) // 10)
        x %= 10
    if x >= 40:
        ans += 'XL'
        x -= 40
    if x >= 10:
        ans += 'X' * (x // 10)
        x %= 10
    # <= 10
    if x >= 9:
        ans += 'IX'
        x -= 9
    if x >= 5:
        ans += 'V' + 'I' * (x - 5)
        x = 0
    if x >= 4:
        ans += 'IV'
        x -= 4
    if x >= 1:
        ans += 'I' * x
    print(ans)
    return
# main
if ord(s[0]) >= ord('A'): rom_to_int()
else: int_to_rom()

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100,  https://codeforces.com/problemset/problem/158/B



思路：

优先安排人数为4和3的组，然后把人数为1的组和3的组尽可能排满，再把人数为2的组两两排满，最后排1的组。

代码

```python
n = int(input())
a = list(map(int, input().split()))
num = [0] * 5
for i in a:
    num[i] += 1
ans = num[4] + num[3]
num[1] = max(0, num[1] - num[3])
ans += num[2] // 2
if num[2] % 2:
    ans += 1
    num[1] = max(0, num[1] - 2)
ans += (num[1] + 3) //4
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

收获：
排队这道题开始有想到一段内的数可以随意交换，但是没有考虑首位最小的贪心；在参考题解后豁然开朗，同时用链表来优化题解中的做法，拓展了自己的思路。
练习了math（M21532:数学密码）、dp（最长上升子序列），熟悉了相应题型。
有一些pythonic的小技巧，包括字符串的拼接‘+’‘*’、join函数；输出的时候可以用 f'n={n}'这样的语句简化代码；还有A if check==True else B这样的表达式。

**T25353 排队**

http://cs101.openjudge.cn/practice/25353/

思路：
贪心：字典序最小必要第一位上最小；同时注意到有类似图的“联通”性质——与最高mx和最低mn距离都不超过d的同学可以移到最前面——将这些人放入tmp数组，进行sort排序。
每次需要把放入tmp数组的人从待选列表中去除，用链表可以实现，去除只需把i的pre连到i的next上即可。

```python
n, d = map(int, input().split())
ans = []
q = []
for i in range(n):
    q.append([int(input()), i - 1, i + 1]) # hi,pre,next
start = 0
tail = n
while start != tail:
    tmp = []
    mn = q[start][0]
    mx = q[start][0]
    flag = 0
    i = start
    while i != tail:
        x = q[i][0]
        if mx - d <= x <= mn + d:
            tmp.append(x)
            if i == start:
                start = q[i][2]
            else:
                q[q[i][1]][2] = q[i][2]
                if q[i][2] == tail:
                    tail = i
                else:
                    q[q[i][2]][1] = q[i][1]
        mn = min(mn, x)
        mx = max(mx, x)
        if mx - mn > d * 2:
            break
        i = q[i][2]
    ans.extend(sorted(tmp))
print(*ans, sep='\n')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)

