from collections import defaultdict

for _ in range(int(input())):
    dic = defaultdict(int)
    for _ in range(int(input())):
        s, a, b = input().split()
        for i in range(int(a), int(b)):
            dic[i] += 1
    print(''.join(chr(v + ord('A') - 1) for _, v in sorted(dic.items())))