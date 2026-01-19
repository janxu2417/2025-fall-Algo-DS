k = int(input())
s = input()
k %= 26
for i in s:
    if ord(i) >= ord('a'):
        print(chr(ord('a') + (ord(i) - ord('a') - k + 26) % 26), end='')
    else:
        print(chr(ord('A') + (ord(i) - ord('A') - k + 26) % 26), end='')
