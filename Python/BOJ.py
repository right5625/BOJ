for _ in range(int(input())):
    s1, s2 = input().split()
    res = sum(ord(i) - ord(j) for i, j in zip(s1, s2))
    print(
        f"Swapping letters to make {s1} look like {s2} {'was FREE.' if res == 0 else f'earned {res} coins.' if res > 0 else f'cost {res * -1} coins.'}"
    )
