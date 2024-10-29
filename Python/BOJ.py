lst1 = [0] * 26
for i in input():
    lst1[ord(i) - ord("a")] += 1
lst2 = [0] * 26
for i in input():
    lst2[ord(i) - ord("a")] += 1
print("".join(chr(ord("a") + i) * max(lst1[i], lst2[i]) for i in range(26)))
