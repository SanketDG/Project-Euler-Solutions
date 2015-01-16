def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

for _ in xrange(int(raw_input())):
    pfs = prime_factors(int(raw_input()))
    # The largest element in the prime factor list
    largest_prime_factor = max(pfs)
    print largest_prime_factor
