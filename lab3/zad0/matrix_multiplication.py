import numpy as np
import sys


def read_matrix_from_input(message="", number_converter=float):
    n, m = map(int, input(message).split())
    a = np.zeros((n, m))
    for i in range(n):
        a[i] = [number_converter(x) for x in input().split()]
    return a


def multiply(a, b):
    n, k = a.shape
    if k != b.shape[0]:
        raise ArithmeticError("Second dimension of first matrix and first dimension of second matrix should be equal.")
    m = b.shape[1]
    c = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            for l in range(k):
                c[i][j] += a[i][l] * b[l][j]
    return c


def main():
    try:
        a = read_matrix_from_input("Give dimensions of first matrix n, m and then n lines with m numbers\n")
        b = read_matrix_from_input("Give dimensions of second matrix n, m and then n lines with m numbers\n")
        print(multiply(a, b))
    except Exception as exception:
        print(sys.exc_info()[0].__name__ + ":", exception, file=sys.stderr)


if __name__ == "__main__":
    main()