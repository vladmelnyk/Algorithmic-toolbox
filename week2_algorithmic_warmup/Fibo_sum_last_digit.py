n = int(input())
n=(n)%60
if n <= 1:
    print(n)
else:

    previous = 0
    current  = 1
    sum=1
    for _ in range(n-1):
        previous, current = current, (previous + current)%10
        sum+=current

    print(sum%10)




