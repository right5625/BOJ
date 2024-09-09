n, k, T0 = map(int, input().split())
T = [T0]
print(
    sum(
        [
            abs(i - k)
            for i in [
                T[-1] + i - abs(T[-1] - k) if T[-1] > k else T[-1] + i + abs(T[-1] - k)
                for i in list(map(int, input().split()))
            ]
        ]
    )
)
