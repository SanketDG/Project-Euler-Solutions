def isPalin(s):
    s = str(s)
    return s[::-1] == s


for _ in xrange(int(raw_input())):
    s = raw_input()
    n = int(s)
    maximum = 1
    for i in xrange(999, 100, -1):
        for j in xrange(i, 100, -1):
            palin = i * j
            if isPalin(palin) and palin < n and palin > maximum:
                maximum = palin
                break
    print maximum
