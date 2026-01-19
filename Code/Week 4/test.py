'''
        01000001 = 41h = ASCII upper-case letter 'A'
 OR      00100000 = 20h <-- this is the bit we want turned on
        -------
EQUALS  01100001 = 61h = ASCII lower-case letter 'a'
'''
x = ~0x7F
print(x)
print(~x + 1)
# 'A' 转换为 'a'
uppera = ord('A')
lowera = uppera | 0x20    # bitwise OR with 20h
print(chr(lowera))  # 输出: a

lowera = uppera  |  (1<<5)
print(chr(lowera))  # 输出: a

# 'a' 转换为 'A'
lowera = ord('a')
uppera = lowera  &  ~0x20    # bitwise AND with 10111111
print(chr(uppera))  # 输出: A

uppera = lowera  &  ~(1<<5)
print(chr(uppera))  # 输出: A