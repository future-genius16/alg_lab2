import time

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

def generate_nested_rectangles(n):
    coms = []
    for i in range(n):
        x1, y1 = 10 * i, 10 * i
        x2, y2 = 10 * (2 * n - i), 10 * (2 * n - i)
        coms.append(Comp(x1, y1, x2, y2))
    return coms

def generate_distributed_points(m, p1, p2, max_coord):
    points = []
    for i in range(m):
        x = (p1 * i) * 31 % max_coord
        y = (p2 * i) * 31 % max_coord
        points.append(Coord(x, y))
    return points


n = int(input("Введите n: "))
m = int(input("Введите m: "))

coms = generate_nested_rectangles(n)

p1, p2 = 10007, 10009
max_coord = 20 * n
points = generate_distributed_points(m, p1, p2, max_coord)

start_time = time.perf_counter()
x_coords, y_coords = [], []
for r in coms:
    x_coords.extend([r.x1, r.x2])
    y_coords.extend([r.y1, r.y2])
for p in points:
    x_coords.append(p.x)
    y_coords.append(p.y)
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
end_time = time.perf_counter()
execution_time = end_time - start_time

print("\nВремя выполнения: {:.6f} секунд".format(execution_time))