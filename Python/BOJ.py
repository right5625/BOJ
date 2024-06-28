S = list(input().split())
dic = {'true' : True, 'false' : False}
if S[1] == 'AND':
    print('true' if dic[S[0]] and dic[S[2]] else 'false')
else:
    print('true' if dic[S[0]] or dic[S[2]] else 'false')