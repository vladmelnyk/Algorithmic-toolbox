# Uses python3

import numpy as np
import sys


def lcs2(a, b):
    temp = np.zeros(shape=(len(a) + 1, len(b) + 1), dtype=int)
    max = 0

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                temp[i, j] = 1 + temp[i - 1, j - 1]
                if max < temp[i, j]:
                    max = temp[i, j]
            else:
                temp[i, j] = 0

    return max


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

    # print(lcs2("commo", "mmorpg"))
