def isPalin(s):
    s = str(s)
    return s[::-1] == s


for _ in xrange(int(raw_input())):
    s = raw_input()
    n = int(s)
    max = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            palin = i * j
            if isPalin(palin) and palin < n:
                if palin > max:
                    max = palin
                    break
    print max
