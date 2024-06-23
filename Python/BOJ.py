for _ in range(int(input())):
    res = 0
    for i in list(''.join(list(input().split())[1:]).split('O')):
        res = max(res, len(i))
    print("The longest contiguous subsequence of X's is of length", res)