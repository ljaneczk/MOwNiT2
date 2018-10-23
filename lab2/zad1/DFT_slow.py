#!/usr/bin/python3
import numpy as np
from common.common import get_value, round_ft_vector


def get_input():
    split_line = input().split()
    n = get_value(split_line[0])
    row = [get_value(x) for x in split_line[1:]]
    while len(row) < n:
        for string in input().split():
            row.append(get_value(string))
    return n, row[:n]


def dft(N, x):
    F = [[np.exp(-2j * np.pi * k * m / N) for k in range(0, N)] for m in range(0, N)]
    return np.dot(F, x)


def main():
    n, x = get_input()
    dft_result = dft(n, x)
    rounded_dft_result = round_ft_vector(dft_result, k=4)
    print(rounded_dft_result)


if __name__ == "__main__":
    main()