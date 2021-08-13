from typing import List


def roman_to_int(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    trans = [d[char] for char in s[::-1]]
    res = [trans[0]]
    for num in trans[1:]:
        if num < abs(res[-1]):
            res.append(-num)
        else:
            res.append(num)
    return sum(res)


def int_to_roman(n: int) -> str:
    units = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    subs = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    return "".join(units.get(x, subs.get(x)) for x in powers_of_ten(n))


def powers_of_ten(n: int) -> List[int]:
    x, i = n, 0
    res = []
    while x > 0:
        x, d = divmod(x, 10)
        if d in (4, 9):
            res.append(d * 10**i)
        elif 5 <= d < 9:
            fives, ones = divmod(d, 5)
            res.extend([5 * 10**i] * fives)
            res.extend([10**i] * ones)
        else:
            res.extend([10**i] * d)
        i += 1
    return sorted(res)[::-1]


print(roman_to_int("III"), 3)
print(roman_to_int("IV"), 4)
print(roman_to_int("IX"), 9)
print(roman_to_int("LVIII"), 58)
print(roman_to_int("XLV"), 45)
print(roman_to_int("MCMXCIV"), 1994)

print(int_to_roman(3), "III")
print(int_to_roman(4), "IV")
print(int_to_roman(9), "IX")
print(int_to_roman(58), "LVIII")
print(int_to_roman(45), "XLV")
print(int_to_roman(1994), "MCMXCIV")
