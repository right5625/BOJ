A = list(input().split())
B = input()
res = 0
for i in A:
    if i != B and i[:len(B)] == B:
        res += 1
print(res)