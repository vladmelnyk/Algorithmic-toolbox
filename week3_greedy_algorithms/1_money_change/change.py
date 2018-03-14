# Uses python3
import sys

def get_change(m):
    big = 10
    medium = 5
    small = 1
    result = 0

    coins = [big, medium, small]

    while m != 0:
        for coin in coins:
            if (m - coin >= 0):
                m -= coin
                result = result+1
                break



    return result

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
