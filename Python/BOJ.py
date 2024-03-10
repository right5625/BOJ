for _ in range(int(input())):
    res = {i : 0 for i in ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']}
    s = input()
    for i in range(38):
        res[s[i:i + 3]] += 1
    print(*res.values())