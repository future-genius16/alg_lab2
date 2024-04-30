class Comp:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Event:
    def __init__(self, val, start, end, ending):
        self.val = val
        self.start = start
        self.end = end
        self.ending = ending

class Node:
    def __init__(self, l_node, r_node, left, right, all):
        self.l_node = l_node
        self.r_node = r_node
        self.left = left
        self.right = right
        self.all = all

class PS_Tree:
    def __init__(self, event_list, size):
        self.nodes = []
        self.root = self.new_tree(0, size)
        val = event_list[0].val
        for event in event_list:
            if event.val != val:
                self.nodes.append(self.root)
                val = event.val
            self.root = self.new_node(self.root, event.start, event.end, event.ending)

    def new_tree(self, left, right):
        if right - 1 == left:
            return Node(None, None, left, right, 0)
        middle = (left + right) // 2
        left = self.new_tree(left, middle)
        right = self.new_tree(middle, right)
        return Node(left, right, left.left, right.right, left.all + right.all)

    def new_node(self, current_node, l, r, val):
        if l <= current_node.left and r >= current_node.right:
            return Node(current_node.l_node, current_node.r_node, current_node.left, current_node.right,
                        current_node.all + val)
        if current_node.left >= r or current_node.right <= l:
            return current_node
        new_node = Node(current_node.l_node, current_node.r_node, current_node.left, current_node.right,
                        current_node.all)
        new_node.l_node = self.new_node(new_node.l_node, l, r, val)
        new_node.r_node = self.new_node(new_node.r_node, l, r, val)
        return new_node

    def find_val(self, index, query):
        return self.search_val(self.nodes[index], query)

    def search_val(self, current_node, query):
        if current_node is None:
            return 0
        middle = (current_node.left + current_node.right) // 2
        if query < middle:
            return current_node.all + self.search_val(current_node.l_node, query)
        else:
            return current_node.all + self.search_val(current_node.r_node, query)

class PT_Alg:
    def __init__(self):
        self.compressed_x = None
        self.compressed_y = None
        self.tree = None

    def start(self, comps):
        if comps:
            self.compr_x, self.compr_y, = compress(comps)
            d_compr_x, d_compr_y = compressed_dicts(self.compr_x, self.compr_y)
            event_list = []
            for r in comps:
                event_list.append(Event(d_compr_x[r.x1], d_compr_y[r.y1], d_compr_y[r.y2], 1))
                event_list.append(Event(d_compr_x[r.x2], d_compr_y[r.y1], d_compr_y[r.y2], -1))
            self.tree = PS_Tree(sorted(event_list, key=lambda e: e.val), len(self.compr_y))

    def count(self, x, y):
        if self.compr_x:
            x = bin(x, self.compr_x)
            y = bin(y, self.compr_y)
            if x == -1 or y == -1 or len(self.tree.nodes) <= x:
                return 0
            else:
                return self.tree.find_val(x, y)
        else:
            return 0

def compress(comps):
    set_x = set()
    set_y = set()
    for r in comps:
        set_x.add(r.x1)
        set_y.add(r.y1)
        set_x.add(r.x2)
        set_y.add(r.y2)
    return list(sorted(set_x)), list(sorted(set_y))

def compressed_dicts(compr_x, compr_y):
    d_compr_x = {compr_x[x]: x for x in range(len(compr_x))}
    d_compr_y = {compr_y[y]: y for y in range(len(compr_y))}
    return d_compr_x, d_compr_y

def bin(q, a):
    low = 0
    high = len(a)
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] <= q:
            low = mid + 1
        else:
            high = mid
    return low - 1

comps = [Comp(*map(int, input().split())) for _ in range(int(input()))]
points = [list(map(int, input().split())) for _ in range(int(input()))]
res = PT_Alg()
res.start(comps)
for x, y in points:
    print(res.count(x, y), end=' ')

