class Treequence:
    def __init__(self, x, n=0):
        self.root = x
        L, R = 2*x + 1, 3*x + 1
        if n < 9999999:
            self.left = Treequence(L, n+2)
            self.right = Treequence(R, n+2)
        else:
            self.left = L
            self.right = R


def sequence(c: int, x: int):
    while True:
        x = c*x + 1
        yield x


def dbl_linear(n):
    seq2 = sequence(2, 1)
    seq3 = sequence(3, 1)

    i = 0
    u2 = {1}
    u3 = {1}

    while i < n:
        u2.add(next(seq2))
        u3.add(next(seq3))
        print(u2)
        print(u3)
        i += 1

    u = sorted(u2 | u3)

    for idx, val in enumerate(u):
        print(f"{idx}: {val}")

    # return sorted(u)[n]


dbl_linear(10)
