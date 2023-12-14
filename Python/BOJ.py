T = input()
key = ord('C') ^ ord(T[0])
print(*[chr(ord(i) ^ key) for i in T], sep = '')