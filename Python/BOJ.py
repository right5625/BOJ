import re

for _ in range(int(input())):
    S = input()
    res = float("inf")
    for i in range(len(S) - 5):
        for j in range(i + 6, len(S) + 1):
            if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)", S[i:j]):
                res = min(res, j - i)
    print(res if res != float("inf") else 0)
