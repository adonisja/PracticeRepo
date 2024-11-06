import heapq

stones = [1, 2, 17, 19, 12, 25, 53, 42, 33, 31, 12]
heap = [-stone for stone in stones]
print(f'pre-heapified heap: {heap}')
heapq.heapify(heap)
heap = sorted(heap)
print(f'heapified heap: {heap}')

while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    print(f'x = {x}, y = {y}')
    res = abs(y - x)
    if res == 0:
        continue
    else:
        heapq.heappush(heap, res)
    print(heap)
print(heap[0] if len(heap) > 0 else 0)