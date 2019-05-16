import heapq

a = []
heapq.heappush(a, 5)
heapq.heappush(a, 3)
heapq.heappush(a, 10)
heapq.heappush(a, 1)

for i in range(0, len(a)) :
    print(heapq.heappop(a))
