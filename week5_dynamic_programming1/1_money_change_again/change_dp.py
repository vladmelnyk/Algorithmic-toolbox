# Uses python3
import sys
from math import inf


def get_change(m):
    # write your code here
    coins = [1, 3, 4]

    min_number_of_coins = [None] * (m + 1)

    min_number_of_coins[0] = 0

    for i in range(1, m + 1):
        min_number_of_coins[i] = inf
        for whole_coin in coins:
            if i >= whole_coin:
                tmp = min_number_of_coins[i - whole_coin] + 1
                if tmp < min_number_of_coins[i]:
                    min_number_of_coins[i] = tmp
            else:
                break

    return min_number_of_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
