#!/usr/bin/python3
import numpy as np
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from common.common import get_nd_array, read_nd_array_from_input


def lu_doolittle_decompose(a, dtype=float):
    if a.shape[0] != a.shape[1]:
        raise ArithmeticError("Cannot do LU Doolittle decomposition for matrices other than square matrix.")
    n = a.shape[0]
    a1 = get_nd_array(a)
    l = np.zeros((n, n), dtype=dtype)
    u = np.zeros((n, n), dtype=dtype)
    for k in range(n):
        l[k][k] = 1
        for j in range(k, n):
            u[k][j] = a1[k][j] - sum([l[k][s] * u[s][j] for s in range(k)])
        for i in range(k+1, n):
            l[i][k] = (a1[i][k] - sum([l[i][s] * u[s][k] for s in range(k)])) / u[k][k]
    return (l, u) if not isinstance(a, np.matrix) else (np.matrix(l), np.matrix(u))


def agh_superfast_lu(a: np.matrix):
    return lu_doolittle_decompose(a)


def main():
    try:
        a = read_nd_array_from_input("Give dimensions of matrix n, m and then n lines with m numbers\n")
        lu = lu_doolittle_decompose(a)
        print("LU decomposition:", "L:", lu[0], "U:", lu[1], sep='\n')
        print("Is result correct (A = L * U)?", np.allclose(a, np.matrix(lu[0]) * np.matrix(lu[1])))
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()
