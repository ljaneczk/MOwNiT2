""" Functions which are used by different programs """
import numpy as np


POWERS_OF_TWO = [2**n for n in range(60)]


def is_power_of_two(n):
    return n in POWERS_OF_TWO


def get_next_power_of_two(n):
    i = 0
    while POWERS_OF_TWO[i] < n:
        i += 1
    return POWERS_OF_TWO[i]


def get_value(string):
    if type(string) == int or type(string) == float:
        return string
    try:
        return float(string) if '.' in str(string) else int(string)
    except:
        return string


def round_ft_vector(dft_result, round_to=2):
    return [(round(get_value(np.real(value)), round_to) + round(get_value(np.imag(value)), round_to) * 1j) for value in dft_result]


def get_fourier_transformation_input():
    split_line = input().split()
    n = get_value(split_line[0])
    row = [get_value(x) for x in split_line[1:]]
    while len(row) < n:
        for string in input().split():
            row.append(get_value(string))
    return n, row[:n]
