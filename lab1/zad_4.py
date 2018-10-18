def count_good(a, b):
    return (a - b) * (a + b)


def count_bad(a, b):
    return a ** 2 - b ** 2


def prove_it():
    b = 10000000000000.0
    eps = 1.0
    k = 10
    for i in range(k):
        print("Calculating a = " + str(b+eps) + ", b = " + str(b) + ":")
        res_bad = count_bad(b+eps, b)
        res_good = count_good(b+eps, b)
        res_real = 2 * eps * b + eps * eps
        print("                 a  =   " + str(b+eps))
        print("                 b  =   " + str(b))
        print("   Bad  a^2 - b^2   =   " + str(res_bad))
        print("   Good (a-b)*(a+b) =   " + str(res_good))
        print("   Correct result   =   " + str(res_real))
        print("")
        b += 1


if __name__ == "__main__":
    prove_it()