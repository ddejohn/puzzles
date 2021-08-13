x = [1,1,3,3,7,2,2,2,2]

def delete_nth(lst, n):
    res = []
    for x in lst:
        if res.count(x) < n:
            res.append(x)
    return res

print(delete_nth(x, 2))
