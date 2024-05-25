s = input()
print(abs(s.index('@') - s.index('#')) + abs(s.index('#') - s.index('!')) - 1 if s.replace('.', '') in ['@#!', '!#@'] else -1)