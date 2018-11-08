#!/usr/bin/python3
# spd matrix - symmetric positive definite matrix
# Matrix M is spd <=> M^T = M (symmetric) and all eigenvalues are positive
import numpy as np
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from common.common import get_nd_array, read_nd_array_from_input


def is_spd_matrix(a, dtype=float):
    if a.shape[0] != a.shape[1]:
        return False
    n = a.shape[0]
    a1 = get_nd_array(a)
    for i in range(n):
        for j in range(i,n):
            if a1[i][j] != a1[j][i]:
                return False
    w, v = np.linalg.eig(a1)        # w - eigenvalues (lambdas), v - eigenvectors
    return all([lmbd > 0 for lmbd in w])


def agh_superfast_spd_check(a: np.matrix):
    return is_spd_matrix(a)


def main():
    try:
        a = read_nd_array_from_input("Give dimensions of matrix n, m and then n lines with m numbers\n")
        is_spd = is_spd_matrix(a)
        print(("Matrix is spd." if is_spd else "Matrix is not spd."))
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()
