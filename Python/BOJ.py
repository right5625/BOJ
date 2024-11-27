op = [list(input().split()) for _ in range(int(input()))]
res = 0
for i in range(1, 101):
    num = i
    for j in op:
        if j[0] == 'ADD':
            num += int(j[1])
        elif j[0] == 'SUBTRACT':
            num -= int(j[1])
            if num < 0:
                res += 1
                break
        elif j[0] == 'MULTIPLY':
            num *= int(j[1])
        else:
            if num % int(j[1]) != 0:
                res += 1
                break
            num /= int(j[1])
print(res)