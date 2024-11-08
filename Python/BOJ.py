import string

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0:
        break
    S = (d + m + y) % 25 + 1
    print(
        "".join(
            (
                string.ascii_lowercase[(ord(i) - ord("a") + (26 - S)) % 26]
                if i in string.ascii_lowercase
                else i
            )
            for i in input()
        )
    )
