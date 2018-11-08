#!/usr/bin/python3
# Cholesky decomposition of a matrix.
# if matrix A is SPD, then there exists matrix L such that L is lower diagonal and A = L * L^T
import numpy as np
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from common.common import get_nd_array, read_nd_array_from_input
from zad2 import spd_checker


def cholesky_decompose(A, dtype=float):
    if A.shape[0] != A.shape[1]:
        raise ArithmeticError("Cannot do Cholesky decomposition for matrices other than square matrix.")
    if not spd_checker.is_spd_matrix(A):
        raise ArithmeticError("Cannot do Cholesky decomposition for non SPD matrices.")
    n = A.shape[0]
    a = get_nd_array(A)
    l = np.zeros((n, n), dtype=dtype)
    for k in range(n):
        summ = 0
        for s in range(k):
            summ += l[k][s] * l[k][s]
        l[k][k] = np.sqrt(a[k][k] - summ)
        for i in range(k+1, n):
            summ = 0
            for s in range(k):
                summ += l[i][s] * l[k][s]
            l[i][k] = (a[i][k] - summ) / l[k][k]
    return l if not isinstance(A, np.matrix) else np.matrix(l)


def agh_superfast_cholesky(a: np.matrix):
    return cholesky_decompose(a)


def main():
    try:
        a = read_nd_array_from_input("Give dimensions of matrix n, n and then n lines with n numbers\n")
        l = cholesky_decompose(a)
        print("Cholesky decomposition:", "L:", l, "U:", l.transpose(), sep='\n')
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()
