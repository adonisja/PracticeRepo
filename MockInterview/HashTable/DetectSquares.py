from collections import Counter, defaultdict

class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point):
        self.ptsCount[tuple(point)] += 1

    def Count(self, point):
        res = 0
        px, py = point
        for x, y in self.ptsCount:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res = self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

