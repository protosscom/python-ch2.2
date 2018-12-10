# 2진, 8진, 10진, 16진 Literal
a = 23
print(type(a))

b = 0b1101
o = 0o23
h = 0x23

print(b, o, h)

# 3.x에서는 int와 long이 합쳐졌다. 표현범위가 무한대
e = 2**1024
print(type(e))
print(e)
print(e.bit_length())

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))