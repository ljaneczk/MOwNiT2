#!/ust/bin/python3
import numpy as np
from common.common import get_value, round_ft_vector, get_next_power_of_two, is_power_of_two
from zad1.DFT_slow import dft


def get_input():
    split_line = input().split()
    n = get_value(split_line[0])
    row = [get_value(x) for x in split_line[1:]]
    while len(row) < n:
        for string in input().split():
            row.append(get_value(string))
    return n, row[:n]


def fft(N, x):
    if N <= 2 or N % 2 == 1:
        return dft(N, x)
    S = N//2
    y_even = fft(S, x[::2])
    y_odd = fft(S, x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    result = np.concatenate([y_even + factor[:S] * y_odd, y_even + factor[S:] * y_odd])
    return result


def main():
    n, x = get_input()
    fft_result = fft(n, x)
    rounded_fft_result = round_ft_vector(fft_result, k=4)
    print(rounded_fft_result)


if __name__ == "__main__":
    main()