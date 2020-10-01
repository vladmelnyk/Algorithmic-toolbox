# Uses python3
import sys
def calc_period(m):
    previous = 0
    current = 1
    p=0
    for i in range(m*m):
        previous, current = current, previous + current
        first = previous % m
        sec = current % m
        if (first == 0 and sec == 1):
            return int(i+1)

def get_fibonacci_huge_naive(n,m):
    p=calc_period(m)
    n=n%p
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n-1):
        previous, current = current, previous + current
    return current % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
