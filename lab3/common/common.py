import numpy as np


def get_nd_array(a):
    if isinstance(a, np.matrix):
        return a.A
    else:
        return a


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