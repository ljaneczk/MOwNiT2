import numpy as np
from bitstring import BitArray


def check_floats(f):
    f32 = np.float32(f)
    f64 = np.float64(f)
    print("Float32(1/3) and Float64(1/3) are equal? - ", f32 == f64)
    f64_32 = np.float64(np.float32(f))
    print("Float32(1/3) and Float64(Float32(1/3)) are equal? - ", f32 == f64_32)
    print("Float64(1/3) and Float64(Float32(1/3)) are equal? - ", f64 == f64_32)
    print("\nBinary representations of 1/3:")
    bin32 = BitArray(float=f, length=32)
    print("Float32(1/3)           ", bin32.bin)
    bin64 = BitArray(float=f, length=64)
    print("Float64(1/3)           ", bin64.bin)
    bin64 = BitArray(float=np.float64(np.float32(f)), length=64)
    print("Float64(Float32(1/3))  ", bin64.bin)


if __name__ == "__main__":
    check_floats(1/3)