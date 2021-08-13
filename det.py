def size(A):
    return len(A), len(A[0])


def sub_mat(A, c):
    m, n = size(A)
    return [[A[i][j] for j in range(n) if j != c] for i in range(1, m)]


def determinant(A, n=0):
    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for col, coef in enumerate(A[0]):
        det += (-1)**n * coef * determinant(sub_mat(A, col))
        n += 1
    return det


mats = [
    [[5, -1, -7, -5], [-6, -2, -10, 1], [-1, -6, -10, 0], [-9, 0, -8, -6]],
    [[1, 5, 2], [-4, 0, 2], [0, 1, 7]],
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]


for mat in mats:
    print(determinant(mat))
