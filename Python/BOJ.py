import heapq

heap = []
for _ in range(int(input())):
    s, n = input().split()
    heapq.heappush(heap, [int(n), s])
print(heapq.heappop(heap)[1])