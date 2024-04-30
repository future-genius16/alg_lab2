class Comp:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = int(input())
coms = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    coms.append(Comp(x1, y1, x2, y2))

m = int(input())
points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append(Coord(x, y))

for p in points:
    ans = 0
    for r in coms:
        if r.x1 <= p.x < r.x2 and r.y1 <= p.y < r.y2:
            ans += 1
    print(ans, end=' ')
