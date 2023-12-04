lv, t = input().split()
print({'miss' : 0, 'bad' : 200, 'cool' : 400, 'great' : 600, 'perfect' : 1000}[t] * int(lv))