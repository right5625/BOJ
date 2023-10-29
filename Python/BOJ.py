for _ in range(15):
    p = list(input().split())
    for i in ['w', 'b', 'g']:
        if i in p:
            res = {'w' : 'chunbae', 'b' : 'nabi', 'g' : 'yeongcheol'}[i]
print(res)