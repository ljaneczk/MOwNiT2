#!/usr/bin/python3
import numpy as np
from common.common import get_value, round_ft_vector, get_fourier_transformation_input


def dft(N, x):
    F = [[np.exp(-2j * np.pi * k * m / N) for k in range(0, N)] for m in range(0, N)]
    return np.dot(F, x)


def main():
    n, x = get_fourier_transformation_input()
    dft_result = dft(n, x)
    rounded_dft_result = round_ft_vector(dft_result, round_to=4)
    print(rounded_dft_result)


if __name__ == "__main__":
    main()