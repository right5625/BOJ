for i in range(int(input())):
    n, P, Q = map(int, input().split())
    cnt = 0
    for j in sorted(list(map(int, input().split()))):
        Q -= j
        if Q < 0:
            break
        else:
            cnt += 1
    print(f"Case {i + 1}: {min(P, cnt)}")
