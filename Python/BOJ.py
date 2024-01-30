E = [i + 1 for i in range(int(input()))]
while len(E) != 1:
    E = [E[i] for i in range(len(E)) if i % 2 == 1]
print(E[0])