import re

pattern = re.compile(r"(-?\d*)x\^?(\d*)")

polys = [
    "3x^4+9x^3+3x-7",
    "-5x^2+10x+4",
    "12x+2",
    "x^2-x",
    "x+1"
]

def d_poly(f, x):
    terms = [map(lambda n: 1 if not n else -1 if n == "-" else int(n), tup) for tup in pattern.findall(f)]
    return sum((c*k)*x**(k-1) for c, k in terms)


for p in polys:
    print(d_poly(p, 1))
