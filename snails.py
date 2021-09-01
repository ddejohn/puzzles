import random
import copy


def array(n, m=None):
    if not m:
        m = n
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]


def rot90(arr, k=1):
    x = copy.deepcopy(arr)
    for _ in range(k):
        x = [[*t] for t in zip(*x)][::-1]
    return x


def snail_path(arr, items=()):
    if not arr:
        return items
    if len(arr) < 1:
        return items + (*arr[0],)

    for i in range(4):
        items += (*rot90(arr, i)[0][:-1],)
    return snail_path([row[1:-1] for row in arr[1:-1]], items)


def recursive_snail(array):
    return list(snail_path(array))


class Snail:
    def __init__(self, array, direction="cw"):
        self.array = array
        self.spiral_direction = "rdlu" if direction == "cw" else "drul"
        self.directions = self.directions_generator()
        self.trail = self.path_generator()

    def __getitem__(self, tup):
        i, j = tup
        return self.array[i][j]

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.trail)

    def path_generator(self):
        position = (0, 0)
        for direction in self.directions:
            yield self[position]
            position = self.move(direction, position)
        yield self[position]

    def directions_generator(self):
        n = len(self.array) - 1
        turns = ((n - i) for i in range(n) for _ in range(2 + (1 - bool(i))))
        for idx, turn in enumerate(turns):
            yield from (self.spiral_direction[idx % 4] for _ in range(turn))

    def move(self, direction, position):
        x, y = position
        return {"r": (x, y + 1),
                "d": (x + 1, y),
                "l": (x, y - 1),
                "u": (x - 1, y)}[direction]


def object_snail(array):
    if len(array) < 2:
        return array[0]
    return [*Snail(array)]
