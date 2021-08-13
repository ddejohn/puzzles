from copy import deepcopy


def transpose(X):
    return [[*r] for r in zip(*X)]


def prod(A, B):
    return [[sum(x*y for x,y in zip(a,b)) for b in transpose(B)] for a in A]


def ID(n):
    return [[0. if j != i else 1. for j in range(n)] for i in range(n)]


def size(A):
    return len(A), len(A[0])


def sub_mat(A, c):
    m, n = size(A)
    return [[A[i][j] for j in range(n) if j != c] for i in range(1, m)]


def rec_det(A):
    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    # just use the top row
    # for i, coef in enumerate(A[0]):


def determinant(M):
    n = len(M)
    if n == 1:
        return M[0]
    A = deepcopy(M)
    for i in range(n-1):
        T = ID(n)
        for j in range(i, n):
            T[j][i] = -(M[j][i] / M[i][i])
        A = prod(T, A)

    p = 1
    for i in range(n):
        p *= A[i][i]
    
    return p



# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

A = [
    [5, -1, -7, -5],
    [-6, -2, -10, 1],
    [-1, -6, -10, 0],
    [-9, 0, -8, -6]
]

# for row in sub_mat(A, 0):
    # print(row)

print(LUdecomp(A))

# print(determinant(A))
# print(determinant())
