N = int(input())
A = list(map(int, input().split()))
n = 2 if len(list(filter(lambda x: x % 2 == 0, A))) > N // 2 else 1
while True:
    if n not in A:
        print(n)
        break
    n += 2