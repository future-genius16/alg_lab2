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

def generate_comps(n, step=10):
    rectangles = []
    for i in range(n):
        x1, y1 = i * step, i * step
        x2, y2 = (2*n - i) * step, (2*n - i) * step
        rectangles.append(Comp(x1, y1, x2, y2))
    return rectangles

def generate_points(n, p1, p2, max_coord):
    points = []
    for i in range(n):
        x = (p1 * i)*31 % max_coord
        y = (p2 * i)*31 % max_coord
        points.append(Coord(x, y))
    return points

n = int(input("Введите n: "))
m = int(input("Введите m: "))


coms = generate_comps(n)

p1, p2 = 10007, 10009
max_coord = 20 * n
points = generate_points(m, p1, p2, max_coord)

start_time = time.perf_counter()
for p in points:
    ans = 0
    for r in coms:
        if r.x1 <= p.x < r.x2 and r.y1 <= p.y < r.y2:
            ans += 1
    print(ans, end=' ')

end_time = time.perf_counter()
execution_time = end_time - start_time

print("\nВремя выполнения: {:.6f} секунд".format(execution_time))