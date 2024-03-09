s = input()[::-1]
print(s[min([s.find(i) for i in 'aeiou' if s.find(i) != -1]):][::-1] + 'ntry')