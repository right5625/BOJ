N = int(input())
S = input()
print(min([S.count(i) for i in 'BONZSILV'] + [S.count('R') // 2, S.count('E') // 2]))