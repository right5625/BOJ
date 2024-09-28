num = 1
for i in range(2, int(input()) + 1):
    num *= i
print(str(num).count("0"))
