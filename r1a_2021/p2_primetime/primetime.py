def factorable(x, s, ps, ns):
    #log(f"factorable({x}, {s}, {ps}, {ns})")
    # Returns true if x is factorable using primes ps AND sums to s (ns is the number of cards for each prime)
    ns = ns.copy()
    for i, p in enumerate(ps):
        #log(f"test {p}")
        while x % p == 0:
            #log(f"{p} is factor")
            #log(f"x {x} p {p}")
            x //= p
            s -= p
            if x < 0:
                # have exceeded allowed sum
                #log(f"sum exceeded. s {s}")
                return False
            ns[i] -= 1
            if ns[i] < 0:
                # p is a factor, but we are out of cards
                # furthermore, as ps are prime, this is the only possible factoring
                #log(f"out of cards. ns[i] {ns[i]}")
                return False
    #log(f"x {x}, s {s}")
    return x == 1 and s == 0

def solve(ps, ns):
    N = sum([p * n for p, n in zip(ps, ns)])
    # product of 50 cards >= 2**50 > 10**15
    lower_bound = max(1, N - 50 * 499)
    #log(f"N {N} lower_bound {lower_bound}")
    for n in range(N, lower_bound - 1, -1):
        #log("loop")
        if factorable(n, N - n, ps, ns):
            return n
    # no solution
    return 0

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        M = int(input())
        ps = []
        ns = []
        for m in range(1, M + 1):
            p, n = [int(x) for x in input().split(" ")]
            ps.append(p)
            ns.append(n)
        #log(f"=== solving case #{t} ===")
        soln = solve(ps, ns)
        print(f"Case #{t}: {soln}")
