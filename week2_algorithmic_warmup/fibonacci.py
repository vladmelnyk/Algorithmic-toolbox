# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    else:
        f=0
        s=1
        temp=f+s
        for i in range(1,n):
            temp=f+s
            f=s
            s=temp
        return temp
n = int(input())
print(calc_fib(n))
