for _ in range(int(input())):
    words = [input() for _ in range(3)]
    res = 'Yes'
    for i in range(3):
        for j in range(3):
            if i != j and (words[i].startswith(words[j]) or words[i].endswith(words[j])):
                res = 'No'
    print(res)