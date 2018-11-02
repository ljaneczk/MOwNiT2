import numpy as np
import sys
from common import get_nd_array


def read_nd_array_from_input(message="", dtype=float):
    n, m = map(int, input(message).split())
    a = np.zeros((n, m), dtype=dtype)
    for i in range(n):
        a[i] = [dtype(x) for x in input().split()]
    return a


def multiply(a, b, dtype=float):
    if a.shape[1] != b.shape[0]:
        raise ArithmeticError("Second dimension of first matrix and first dimension of second matrix should be equal.")
    n, k = a.shape
    m = b.shape[1]
    a1 = get_nd_array(a)
    b1 = get_nd_array(b)
    c = np.zeros((n, m), dtype=dtype)
    for i in range(n):
        for j in range(m):
            for l in range(k):
                c[i][j] += a1[i][l] * b1[l][j]
    return c if not (isinstance(a, np.matrix) and isinstance(b, np.matrix)) else np.matrix(c)


def agh_superfast_matrix_multiply(a: np.matrix, b: np.matrix) -> np.matrix:
    return multiply(a, b)


def main():
    try:
        a = read_nd_array_from_input("Give dimensions of first matrix n, m and then n lines with m numbers\n")
        b = read_nd_array_from_input("Give dimensions of second matrix n, m and then n lines with m numbers\n")
        c = multiply(a, b)
        print("Result for numpy.ndarray:", c, sep="\n")
        print("Does multiply return the same for numpy.matrix?", np.allclose(c, multiply(np.matrix(a), np.matrix(b))))
        print("Is result correct?", np.allclose(c, np.matrix(a) * np.matrix(b)))
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()