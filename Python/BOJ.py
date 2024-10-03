n = int(input())
b = input()
print(
    b[0]
    + "".join(["1" if (b[i - 1] + b[i]).count("1") == 1 else "0" for i in range(1, n)])
)
