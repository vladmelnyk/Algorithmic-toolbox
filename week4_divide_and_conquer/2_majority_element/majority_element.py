# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    leftMajority = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    rightMajority = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    left_count = 0
    for i in range(left, right):
        if a[i] == leftMajority:
            left_count += 1
    if left_count > (right - left) // 2:
        return leftMajority

    right_count = 0
    for i in range(left, right):
        if a[i] == rightMajority:
            right_count += 1
    if right_count > (right - left) // 2:
        return rightMajority

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

