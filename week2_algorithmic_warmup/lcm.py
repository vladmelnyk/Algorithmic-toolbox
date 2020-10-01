# Uses python3
import sys


def gcd(a, b):
    if (a < b):
        return gcd(b, a)
    elif (b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm_naive(a, b):
    return (a * b) / gcd(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(lcm_naive(a, b)))
