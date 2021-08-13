def listify(*args):
    if len(args) == 1:
        return str(args[0])
    *first_n, last = args
    return ", ".join(map(str, first_n)) + f", and {last}"


def format_duration(s: int) -> str:
    result = []
    remainder = s
    conversions = {"year":    31536000,
                   "day":     86400,
                   "hour":    3600,
                   "minute":  60,
                   "second":  1}

    for word, num_seconds in conversions.items():
        num_epochs, remainder = divmod(remainder, num_seconds)
        if num_epochs > 0:
            result.append(f"{num_epochs} {word}" + "s"*bool(num_epochs - 1))

    return ", ".join(result)


print(format_duration(3600))
