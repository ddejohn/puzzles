import random
import copy


def array(n, m=None):
    if not m:
        m = n
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]


def rot90(arr):
    return [[*t] for t in zip(*arr)][::-1]


def shrink(arr):
    return [row[1:-1] for row in arr[1:-1]]


def tiles(arr):
    r0 = copy.deepcopy(arr)
    r1 = rot90(r0)
    r2 = rot90(r1)
    r3 = rot90(r2)
    return r0, r1, r2, r3


def slice_snail(arr):
    if len(arr) == 2:
        return arr[0] + arr[1][::-1]
    elif len(arr) == 1:
        return arr[0]
    result = []
    r0, r1, r2, r3 = tiles(arr)
    while True:
        result.extend(r0[0][:-1] + r1[0][:-1] + r2[0][:-1] + r3[0][:-1])
        r0, r1, r2, r3 = tiles(shrink(r0))
        if (sq := len(r0) == 1) or (len(r1) == 1):
            if sq:
                result.extend(r0[0])
            else:
                result.extend(r1[0])
            break
        elif not r0:
            break
    return result


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
