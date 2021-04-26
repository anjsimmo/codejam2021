# full revolution in ticks
R = 360 * 12 * 10**10


def solveNAQ(H, M, S, P):
    # Given {H, M, S, P} solve for {N, A, Q}
    #
    # 3 Equations, 3 Unknowns:
    # H = N + A             (1)
    # M = 12*N - R*P + A    (2)
    # S = 720*N - R*Q + A   (3)
    #
    #
    # From (1, 2)
    # M-H = 11*N - R*P
    # N = (M-H + R*P) / 11
    #
    # From (1)
    # A = H-N
    #
    # From (3)
    # Q = (720*N + A - S) / R
    #
    # Constraints:
    # N, A, Q are integers
    # 0 <= N < 10**9 * 60 * 60 * 12
    # -R < A < -R
    # 0 < Q < 60 * 60 * 12
    if (M-H + R*P) % 11 != 0:
        return None
    N = (M-H + R*P) // 11
    if N < 0:
        return None
    if N >= 10**9 * 60 * 60 * 12:
        return None
    A = H-N
    if A >= R:
        return None
    if A <= -R:
        return None
    if (720*N + A - S) % R != 0:
        return None
    Q = (720*N + A - S) // R
    if Q < 0:
        return None
    if Q >= 60 * 60 * 12:
         return None
    return N


def permABC(A, B, C):
    return [
        (A, B, C),
        (A, C, B),
        (B, A, C),
        (B, C, A),
        (C, A, B),
        (C, B, A)
    ]



def to_hmsn(N):
    h = N // (10**9 * 60 * 60)
    N = N % (10**9 * 60 * 60)
    m = N // (10**9 * 60)
    N = N % (10**9 * 60)
    s = N // (10**9)
    N = N % (10**9)
    n = N
    return h, m, s, n


def solve(A, B, C):
    for P in range(0,12):
        for H, M, S in permABC(A, B, C):
            soln = solveNAQ(H, M, S, P)
            if soln is not None:
                # sanity check that our solution is valid
                _h, _m, _s, _n = to_hmsn(soln)
                if _h < 0 or _h >= 12 or _m < 0 or _m >= 60 or _s < 0 or _s >= 60:
                    continue
                return soln
    return None


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        A, B, C = [int(x) for x in input().split(" ")]
        N = solve(A, B, C)
        assert N is not None # According to problem statement, there is at least one solution
        h, m, s, n = to_hmsn(N) 
        print (f"Case #{t}: {h} {m} {s} {n}")
