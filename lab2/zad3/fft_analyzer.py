#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

from common.common import get_fourier_transformation_input
from zad2.FFT_fast import fft


def print_fft_plot(n, fft_result):
    f_s = 1
    freqs = fftpack.fftfreq(n) * f_s
    fig, ax = plt.subplots()
    pos_freqs = [fr for fr in freqs if fr >= 0]

    ax.stem(pos_freqs, np.abs(fft_result[:len(pos_freqs)]))
    ax.set_xlabel('Frequency in edits/year')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    ax.set_ylim(-1, 3000)
    plt.show()


def main():
    n, x = get_fourier_transformation_input()
    fft_result = fft(n, x)
    print_fft_plot(n, fft_result)



if __name__ == "__main__":
    main()