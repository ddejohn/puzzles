words = {1: "One",
         2: "Two",
         3: "Three",
         4: "Four",
         5: "Five",
         6: "Six",
         7: "Seven",
         8: "Eight",
         9: "Nine",
         10: "Ten",
         11: "Eleven",
         12: "Twelve",
         13: "Thirteen",
         14: "Fourteen",
         15: "Fifteen",
         16: "Sixteen",
         17: "Seventeen",
         18: "Eighteen",
         19: "Nineteen",
         20: "Twenty",
         30: "Thirty",
         40: "Forty",
         50: "Fifty",
         60: "Sixty",
         70: "Seventy",
         80: "Eighty",
         90: "Ninety",
         100: "Hundred",
         1000: "Thousand",
         1000000: "Million",
         1000000000: "Billion",
         1000000000000: "Trillion"}


denominations = (1e12, 1e9, 1e6, 1e3, 100, 10)


def get_words(t: tuple) -> str:
    if not t:
        return "Zero"
    return " ".join(get_words(i) if type(i) == tuple else words[i] for i in t)


def num_words(n: int, res=(), den=denominations):
    if n in denominations[:-1]:
        return ((1, n),)
    if n in words:
        return (n,)

    for idx, denomination in enumerate(map(int, den)):
        quotient, remainder = divmod(n, denomination)
        if quotient:
            if quotient * denomination in words:
                res += (*num_words(quotient*denomination),)
            else:
                res += (*num_words(quotient, den=den[idx+1:]), denomination)
            if remainder:
                res += (*num_words(remainder, den=den[idx+1:]),)
            break
    return res


# OLD SOLUTION
# units = (0, 1, 10, 100, 1000, 1000000, 1000000000, 1000000000000)


# def get_word(num: int) -> str:
#     res = words[num]
#     if num in units[3:]:
#         res = f"One {res}"
#     return res


# def num_words(num: int) -> str:
#     if num == 0:
#         return "Zero"
#     if num in words:
#         return get_word(num)
#     res = []
#     while num > 0:
#         for idx, unit in enumerate(reversed(units[1:])):
#             quotient, remainder = divmod(num, unit)
#             if quotient*unit in words:
#                 res.append(get_word(quotient*unit))
#                 num = remainder
#             elif quotient in words:
#                 res.append(f"{get_word(quotient)} {words[unit]}")
#                 num = remainder
#             elif units[idx-1] < quotient < unit:
#                 res.append(f"{num_words(quotient)} {words[unit]}")
#                 num = remainder
#             if remainder in words:
#                 res.append(get_word(remainder))
#                 return " ".join(res)
#     return " ".join(res)


print(f"{0:>12}  ->  {num_words(0)}")
print(f"{1:>12}  ->  {num_words(1)}")
print(f"{10:>12}  ->  {num_words(10)}")
print(f"{12:>12}  ->  {num_words(12)}")
print(f"{110:>12}  ->  {num_words(110)}")
print(f"{111:>12}  ->  {num_words(111)}")
print(f"{211:>12}  ->  {num_words(211)}")
print(f"{123:>12}  ->  {num_words(123)}")
print(f"{1100:>12}  ->  {num_words(1100)}")
print(f"{1234:>12}  ->  {num_words(1234)}")
print(f"{12345:>12}  ->  {num_words(12345)}")
print(f"{100000:>12}  ->  {num_words(100000)}")
print(f"{100100:>12}  ->  {num_words(100100)}")
print(f"{123456:>12}  ->  {num_words(123456)}")
print(f"{567000:>12}  ->  {num_words(567000)}")
print(f"{1234567:>12}  ->  {num_words(1234567)}")
print(f"{12345678:>12}  ->  {num_words(12345678)}")
print(f"{123456789:>12}  ->  {num_words(123456789)}")
print(f"{1234567891:>12}  ->  {num_words(1234567891)}")
