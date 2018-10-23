#!/usr/bin/python3
import numpy as np


def get_value(input):
    try:
        return float(input)
    except:
        try:
            return int(input)
        except:
            return input


def get_input():
    n = int(input())
    row = []
    while len(row) < n:
        for string in input().split():
            row.append(get_value(string))
    return n, row[:n]


def dft(N, x):
    F = [[np.exp(-2j * np.pi * k * m / N) for k in range(0, N)] for m in range(0, N)]
    return np.dot(F, x)


def round_dft(dft_result, k=2):
    return [(round(get_value(np.real(value)), k) + round(get_value(np.imag(value)), k) * 1j) for value in dft_result]


def main():
    n, x = get_input()
    dft_result = dft(n, x)
    rounded_dft_result = round_dft(dft_result, k=4)
    print(rounded_dft_result)


if __name__ == "__main__":
    main()