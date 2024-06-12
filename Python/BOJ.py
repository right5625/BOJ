import string

for i in [input() for _ in range(int(input()))]:
    if sum([i.count(j) for j in string.ascii_uppercase]) <= sum([i.count(j) for j in string.ascii_lowercase]) and len(i) <= 10 and sum([i.count(j) for j in list(map(str, range(10)))]) != len(i):
        print(i)
        break