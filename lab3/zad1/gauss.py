#!/usr/bin/python3
# Gauss computation
import numpy as np
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from common.common import get_nd_array, read_nd_array_from_input, split_nd_array_into_a_b


def gauss_elimination(A, B, dtype=float):
    if A.shape[0] != A.shape[1] or B.shape[0] != A.shape[0] or B.shape[1] != 1:
        raise ArithmeticError("A should have dimensions n by n and B dimensions n by 1 for any n > 0")
    a = get_nd_array(A)
    b = get_nd_array(B)
    n = a.shape[0]
    for k in range(0, n):
        for i in range(k+1, n):
            xmult = a[i][k] / a[k][k]
            a[i][k] = xmult
            for j in range(k+1, n):
                a[i][j] -= xmult * a[k][j]
            b[i] -= xmult * b[k]
    x = np.zeros((n,1))
    x[n-1][0] = b[n-1] / a[n-1][n-1]
    for i in range(n-1, -1, -1):
        summ = b[i]
        for j in range(i+1, n):
            summ -= a[i][j] * x[j][0]
        x[i][0] = summ / a[i][i]
    return np.matrix(x) if isinstance(A, np.matrix) else x


def agh_superfast_gauss(a: np.matrix, b: np.matrix):
    return gauss_elimination(a, b)


def main():
    try:
        A = read_nd_array_from_input("Give dimensions of matrix n, n+1 and then n lines with n+1 numbers\n")
        a, b = split_nd_array_into_a_b(A)
        print(gauss_elimination(a, b))
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()
