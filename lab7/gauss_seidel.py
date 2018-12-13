#!/usr/bin/python3
import numpy as np
from common.common import read_nd_array_from_input, EPS, print_linear_equation
""" Gauss-Seidel iterative method for a * x = b"""
""" Gauss-Seidel iterative method is convergent iff p(D^-1*(L+U)) < 1 """


""" 
    A = (L+D) + U
    D[i][j] = 1/A[i][j] if i == j else 0 
    x(t+1)[i] = 1/A[i][i] * (b[i] - sum(j=1..i-1) { A[i][j] * x(t+1)[j]} - sum(j=i+1..n) { A[i][j] * x(t)[j] }
    :return x^T 
    Note that Jacobi iterative method is convergent iff p(D^-1*(L+U)) < 1
"""
def jacobi_iterative_solve(A, b):
    if A.shape[0] != A.shape[1] or A.shape[1] != b.shape[0]:
        raise ArithmeticError("a should be n * n matrix and b should be n * 1 matrix for some n > 0")
    n = A.shape[0]
    b1 = np.transpose(b)[0]
    x = np.zeros(n)
    while True:
        x1 = np.zeros(n)
        for i in range(n):
            x1[i] = 1 / A[i][i] * (b1[i] - sum([A[i][j] * x1[j] for j in range(i)]) - sum([A[i][j] * x[j] for j in range(i+1,n)]))
        error = sum(abs(np.dot(A, x1.transpose()) - b1))
        #print(x1, x, error, np.dot(A, x1.transpose()) - b1)
        if error < EPS:
            return np.transpose(x1)
        else:
            x = x1


def main():
    A = read_nd_array_from_input("Give dimensions of first matrix n, n and then n lines with n numbers\n")
    b = read_nd_array_from_input("Give dimensions of first matrix n, 1 and then n lines with 1 number\n")
    x = jacobi_iterative_solve(A, b)
    print("Problem to solve: A * x = b")
    print_linear_equation(A, b, x="x")
    print("Solution for A * x = b:", x, sep="\n")


if __name__ == "__main__":
    main()
