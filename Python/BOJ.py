X_lst, Y_lst = [], []
for _ in range(int(input())):
    X, Y = map(int, input().split())
    X_lst.append(X)
    Y_lst.append(Y)
print(max(max(X_lst) - min(X_lst), max(Y_lst) - min(Y_lst)) ** 2)
