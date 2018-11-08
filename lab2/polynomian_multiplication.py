import numpy.fft as np
from numpy import real as rl


def count(a, b):
    a = list(reversed(a))
    b = list(reversed(b))
    while len(a) < len(b):
        a.append('0')
    while len(b) < len(a):
        b.append('0')
    a += (['0' for i in range(len(a))])
    b += (['0' for i in range(len(b))])
    ad = [int(x) for x in list(a)]
    bd = [int(x) for x in list(b)]
    res = np.ifft(np.fft(ad) * np.fft(bd))
    res = [int(rl(x)) for x in res]
    c = ""
    cur = 0
    for v in res:
        c += str((cur + v) % 10)
        cur = (cur + v) // 10
    while cur > 0:
        c += str((cur) % 10)
        cur = (cur) // 10
    while c[len(c)-1] == '0':
        c = c[:-1]
    return c[::-1]


def main():
    t = int(input())
    while t > 0:
        a, b = input().split()
        minus = (a[0] == '-' and b[0] != '-') or (a[0] != '-' and b[0] == '-')
        if a[0] == '-':
            a = a[1:]
        if b[0] == '-':
            b = b[1:]
        res = count(a, b)
        if minus:
            res = '-' + res
        print(res)
        t -= 1


if __name__ == "__main__":
    main()