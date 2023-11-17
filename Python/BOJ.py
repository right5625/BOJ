import heapq

a1, a2, a3, b1, b2, b3, L = map(int, input().split())
heap = [-a1] * b1 + [-a2] * b2 + [-a3] * b3
heapq.heapify(heap)
l = res = 0
while l < L:
    if not heap:
        res = 0
        break
    l += -heapq.heappop(heap)
    res += 1
print(res)