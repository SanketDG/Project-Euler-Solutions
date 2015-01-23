for _ in xrange(int(raw_input())):
    x = int(raw_input())

    prev, cur = 0, 1
    total = 0
    while True:
        prev, cur = cur, prev + cur
        if cur >= x:
            break
        if cur % 2 == 0:
            total += cur
    print total
