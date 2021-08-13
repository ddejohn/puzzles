import timeit


def mag(n: int, i: int = 0) -> int:
    if n % 10 == n:
        return i
    return mag(n // 10, i+1)


def ddejohn(n: int) -> str:
    expanded = []

    while True:
        exp = len(str(n))-1
        coef, n = divmod(n, 10**exp)
        if coef == 0:
            break
        expanded.append(f"{coef}" + "0"*exp)
        if exp == 0:
            break

    return " + ".join(expanded)


def clownfragment(num):
    return ' + '.join(reversed([n + ('0'*idx) for idx, n in enumerate(reversed(str(num))) if n != '0']))


def lanceypantsy(num):
    num_str = str(num)
    out_str = ''
    if len(num_str) == 1:
        return str(num)
    for i, digit in enumerate(reversed(num_str)):
        if digit == '0':
            continue
        if i == 0:
            out_str += digit + ' + '
        elif i == len(num_str) - 1:
            out_str += str(0)*i + digit
        else:
            out_str += str(0)*i + digit + ' + '
    return out_str[::-1]


def alex_m(num):
    lst = [int(nums) for nums in str(num)]
    max_num = '0' * (len(lst) - 1)
    out = []
    for number in lst:
        out.append(str(number) + max_num)
        max_num = max_num[:-1]
    out2 = []
    for value in out:
        if len(str(value)) > 1:
            if int(value) != 0:
                out2.append(value)
    final = str()
    for values in out:
        final += str(values) + ' ' + '+' + ' '
    return final[:-2]


t1 = timeit.timeit(
    "ddejohn(78251231)",
    number=1000000,
    globals=globals()
)


t2 = timeit.timeit(
    "clownfragment(78251231)",
    number=1000000,
    globals=globals()
)


t3 = timeit.timeit(
    "lanceypantsy(78251231)",
    number=1000000,
    globals=globals()
)


t4 = timeit.timeit(
    "alex_m(78251231)",
    number=1000000,
    globals=globals()
)


print(f"ddejohn: {t1}\nclownfragment: {t2}\nlanceypantsy: {t3}\nalex_m: {t4}")
