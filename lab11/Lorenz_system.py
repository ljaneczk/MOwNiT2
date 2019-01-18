import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint


sigma, rho, beta = 10, 99.96, 8/3
# sigma, rho, beta = 10, 28, 8/3


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z


def lorenz_system(init_state, t, sigma1=sigma, rho1=rho, beta1=beta):
    global sigma, rho, beta
    sigma, rho, beta = sigma1, rho1, beta1
    states = odeint(f, init_state, t)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(states[:, 0], states[:, 1], states[:, 2])
    plt.show()


def main():
    global sigma, rho, beta
    cin = input("Give sigma, rho and beta separated by spaces or def in case of default: ")
    if cin != "def":
        sigma, rho, beta = \
            map(lambda x: float(x), cin.split())
    init_state = [1, 1, 1]
    t = np.arange(0, 40, 0.01)
    lorenz_system(init_state, t, sigma, rho, beta)


if __name__ == "__main__":
    main()
