import matplotlib.pyplot as plt
import numpy as np


def print_distances(l, r, n):
    values = np.linspace(l, r, n)   # from l to r generate n numbers with equal distances
    distances = []
    for i in values:
        distances.append(np.spacing(i))         # np.spacing(i) - min esp such i+eps is next float after i
    plt.plot(values, distances)
    plt.show()


if __name__ == "__main__":
    print_distances(1.0, 1000.0, 1000000)