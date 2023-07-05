import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
graph = [[sys.maxsize for __ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w
vst = [False] * (V + 1)
heap = [(0, 1)] # 거리, 정점
res = 0
while heap:
    w, s = heapq.heappop(heap)
    if not vst[s]:
        vst[s] = True
        res += w
        for e in range(1, V + 1):
            if graph[s][e] != 0 and not vst[e]: # s 정점과 연결되어 있는 모든 정점 중 아직 방문하지 않은 정점을 선택
                heapq.heappush(heap, (graph[s][e], e)) # 선택된 정점의 가중치를 우선순위로 지정하여 힙에 삽입
print(res)