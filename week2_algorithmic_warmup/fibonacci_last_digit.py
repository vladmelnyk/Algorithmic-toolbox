def solution(num):
    n=num%60
    if n <= 1:
       return(n)

    previous = 0
    current = 1

    for _ in range(1,n):
        previous, current = current, previous + current

    return (current % 10)

if __name__ == "__main__":
    inp=int(input())
    print(solution(inp))