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


def round_ft_vector(dft_result, k=2):
    return [(round(get_value(np.real(value)), k) + round(get_value(np.imag(value)), k) * 1j) for value in dft_result]
