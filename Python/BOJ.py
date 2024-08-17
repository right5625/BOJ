n, m = map(int, input().split())
task = [list(map(int, input().split())) for _ in range(n)]
weights = [1 if task[0][i] else 0 for i in range(m)]
scores = [sum([weights[j] * task[i][j] for j in range(m)]) for i in range(n)]
print(1, scores.count(scores[0]))