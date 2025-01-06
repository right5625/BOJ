S = [i for i in input() if i in 'aeiou']
print('S' if S == S[::-1] else 'N')