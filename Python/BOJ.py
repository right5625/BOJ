import heapq

heap = []
for _ in range(int(input())):
    A, B = input().split()
    heapq.heappush(heap, (-int(B), A))
print(heapq.heappop(heap)[1])