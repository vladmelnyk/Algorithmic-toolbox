# Uses python3

import sys

import math


def is_greater(digit, max_digit):
    return digit + max_digit > max_digit + digit


def largest_number(digits):
    # write your code here
    res = ""

    while len(digits) != 0:
        max_digit = '0'
        for digit in digits:
            # print("digit str ", digit_str)
            if is_greater(digit, max_digit):
                max_digit = digit
                # print("max", max_digit)
        res += max_digit
        # print(max_digit)
        digits.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
