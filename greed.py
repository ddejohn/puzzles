scoring = {
    (1,1,1): 1000,
    (2,2,2): 200,
    (3,3,3): 300,
    (4,4,4): 400,
    (5,5,5): 500,
    (6,6,6): 600,
    (1,): 100,
    (5,): 50
}

def score(dice):
    d = dice.copy()

    parts = []
    for x in set(dice):
        n = d.count(x)
        if n >= 3:
            parts.append((x,)*3)
            if x in [1,5] and n-3 > 0:
                parts.extend([(x,)]*(n-3))
        elif x in [1,5]:
            parts.extend([(x,)]*n)
            
    return sum(scoring.get(t, 0) for t in parts)


print(score([2, 3, 4, 6, 2]))
print(score([4, 4, 4, 3, 3]))
print(score([2, 2, 4, 5, 2]))
print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
print(score([2, 4, 4, 5, 4]))
print(score([4, 4, 4, 4, 4]))
print(score([5, 5, 5, 5, 5]))
