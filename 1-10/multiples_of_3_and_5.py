def sum_series(i, n):
    num = n / i
    sum = (num * i * (num + 1)) / 2
    return int(sum)

T = int(raw_input())
for _ in range(T):
    N = int(raw_input()) - 1
    print sum_series(3, N) + sum_series(5, N) - sum_series(15, N)
