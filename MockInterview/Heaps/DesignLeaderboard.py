from heapq import heappush, heappop
from collections import defaultdict

class LeaderBoard:
    def __init__(self) -> None:
        self.scores = defaultdict(int)
        self.minHeap = []

    def AddScore(self, playerID, score):
        self.scores[playerID] += score

    def resetScore(self, playerID):
        del self.scores[playerID]

    def top(self, k):
        res = 0
        for score in self.scores.values():
            if len(self.minHeap) < k:
                heappush(self.minHeap, score)
            else:
                if score > self.minHeap[0]:
                    heappop(self.minHeap)
                    heappush(self.minHeap, score)
        
        for num in self.heap:
            res += num
        return res
