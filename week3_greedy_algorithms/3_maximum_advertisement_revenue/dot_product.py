# Uses python3

import sys

def max_dot_product(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append((a[i] * b[j]))

    c.sort()
    c = c[-len(a):]

    return sum(c)
def max_dot_product_fast(a, b):
    a.sort()
    b.sort()

    c = []
    for i in range(len(a)):
        c.append(a.pop()*b.pop())

    return sum(c)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product_fast(a, b))
