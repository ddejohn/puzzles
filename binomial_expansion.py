import re

pattern = re.compile(r"\((-?\d*)(\w)[+]?(-?\d*)\)\^(\d*)")


def fac(n: int) -> int:
    return 1 if n < 2 else n * fac(n-1)


def nCk(n: int, k: int) -> int:
    return fac(n) // (fac(k) * fac(n-k))


# some of the ugliest code I've ever written
def expand(expr):
    a, x, y, n = pattern.match(expr).groups()

    if n == 0:
        return "1"
    elif n == 1:
        sign = "+" if y > 0 else ""
        a = a if abs(a) > 1 else ""
        return f"{a}{x}{sign}{y}"
    
    out = ""
    a = 1 if not a else -1 if a == "-" else a
    a, y, n = [int(val) for val in [a, y, n]]

    for i in range(n+1):
        k = n - i
        coef = nCk(n, i) * a**(k) * y**i

        sign = "+" if coef > 0 else ""
        if k != 0 and abs(coef) == 1:
            coef = "" if coef > 0 else "-"

        p = f"{x}^{k}" if k > 1 else f"{x}"*k
        out += f"{sign}{coef}{p}"

    return out.lstrip("+")


exprs = [
    ("(x+1)^0", "1"),
    ("(x+1)^1", "x+1"),
    ("(x+1)^2", "x^2+2x+1"),
    ("(x-1)^0", "1"),
    ("(x-1)^1", "x-1"),
    ("(x-1)^2", "x^2-2x+1"),
    ("(5m+3)^4", "625m^4+1500m^3+1350m^2+540m+81"),
    ("(2x-3)^3", "8x^3-36x^2+54x-27"),
    ("(7x-7)^0", "1"),
    ("(-5m+3)^4", "625m^4-1500m^3+1350m^2-540m+81"),
    ("(-2k-3)^3", "-8k^3-36k^2-54k-27"),
    ("(-7x-7)^0", "1")
]


for expr, truth in exprs:
    print(expand(expr))
    print(truth)
    print()
