res = 0
input()
while True:
    S = input()
    if S == '고무오리 디버깅 끝':
        print('힝구' if res else '고무오리야 사랑해')
        break
    elif S == '문제':
        res += 1
    else:
        res += -1 if res else 2