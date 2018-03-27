# Uses python3
import sys
from math import inf


def func1(x): return (int)(x - 1)


def func2(x): return (int)(x / 2)


def func3(x): return (int)(x / 3)


actions = [func1, func2, func3]


def optimal_sequence(m):
    min_sequence = [None] * (m + 1)

    min_sequence[0] = 0
    min_sequence[1] = 0

    sequence = []
    sequence.append([0])
    sequence.append([1])

    # 1 2 3 4 5 6 7 8 9 10
    # 1 1 1 2 3 2 3 3 2 3
    for i in range(2, m + 1):
        min_sequence[i] = inf
        tmp2 = inf
        tmp3 = inf
        if (i % 3 == 0):
            tmp3 = min_sequence[func3(i)] + 1
        if (i % 2 == 0):
            tmp2 = min_sequence[func2(i)] + 1
        tmp1 = min_sequence[i - 1] + 1

        min_tmp = min(tmp1, tmp2, tmp3)

        min_sequence[i] = min_tmp
        if min_tmp == tmp1:
            sequence.append(sequence[func1(i)] + [i])
            continue
        if min_tmp == tmp2:
            sequence.append(sequence[func2(i)] + [i])
            continue
        if min_tmp == tmp3:
            sequence.append(sequence[func3(i)] + [i])

    return sequence[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
