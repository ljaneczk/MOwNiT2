import numpy as np


def get_nd_array(a):
    if isinstance(a, np.matrix):
        return a.A
    else:
        b = np.copy(a)
        return b


def convert_nd_array_to_matrix(a):
    return np.matrix(a)


def convert_matrix_to_nd_array(a: np.matrix):
    return a.A


def read_nd_array_from_input(message="", dtype=float):
    n, m = map(int, input(message).split())
    a = np.zeros((n, m), dtype=dtype)
    for i in range(n):
        a[i] = [dtype(x) for x in input().split()]
    return a


def read_matrix_from_input(message="", dtype=float):
    return np.matrix(read_nd_array_from_input(message, dtype))


def split_nd_array_into_a_b(A):
    A = get_nd_array(A)
    if A.shape[1] == 1:
        raise Exception("Cannot separate column from n by 1 matrix")
    n, m = A.shape
    a = np.ndarray((n, m-1))
    b = np.ndarray((n, 1))
    for i in range(n):
        for j in range(m-1):
            a[i][j] = A[i][j]
        b[i] = A[i][m-1]
    return a, b