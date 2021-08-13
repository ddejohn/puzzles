import re

def strip_comments(lines: str, markers: list):
    if not markers:
        return lines
    comments = r"".join(f"\\{c}" for c in markers)
    return re.sub(f"( *[{comments}].*)", "", lines)


# print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
# print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]))
# print(strip_comments('^ lemons\ncherries apples\napples strawberries\nlemons ? pears #\navocados pears pears oranges bananas cherries', ['-', '=', '^', '?', '.']))
print(strip_comments('bananas cherries lemons apples lemons cherries\noranges watermelons avocados\n, strawberries lemons avocados avocados\n- lemons @ . pears avocados', ['#', '^', "'", '?', '!', '@']))