idx = 0
for i in input():
    if i == 'KOREA'[idx % 5]:
        idx += 1
print(idx)