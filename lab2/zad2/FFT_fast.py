#!/ust/bin/python3
import numpy as np
from common.common import *
from zad1.DFT_slow import dft


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
    n, x = get_fourier_transformation_input()
    fft_result = fft(n, x)
    rounded_fft_result = round_ft_vector(fft_result, round_to=4)
    print(rounded_fft_result)


if __name__ == "__main__":
    main()