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

def compress(coords):
    sorted_coords = sorted(set(coords))
    mapping = {coord: i for i, coord in enumerate(sorted_coords)}
    return mapping

n = int(input())
x_coords, y_coords = [], []
coms = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x_coords.extend([x1, x2])
    y_coords.extend([y1, y2])
    coms.append(Comp(x1, y1, x2, y2))

m = int(input())
points = []
for _ in range(m):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)
    points.append(Coord(x, y))

x_map = compress(x_coords)
y_map = compress(y_coords)

grid = [[0] * len(y_map) for _ in range(len(x_map))]

for r in coms:
    for i in range(x_map[r.x1], x_map[r.x2]):
        for j in range(y_map[r.y1], y_map[r.y2]):
            grid[i][j] += 1

for p in points:
    x, y = x_map[p.x], y_map[p.y]
    print(grid[x][y], end=' ')
