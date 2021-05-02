
def gap_start(a):
    return [a - 1]

def gap_end(b, K):
    return [K - b]

def gap_mid(a, b):
    gap = b - a - 1
    if gap <= 0:
        return [0]
    win = 1 + (gap - 1) // 2
    extra = gap - win
    return [win, extra]

def solve(N, K, P):
    P = sorted(P)
    gaps = []
    gaps += gap_start(P[0])
    for a, b in zip(P, P[1:]):
        gaps += gap_mid(a, b)
    gaps += gap_end(P[-1], K)
    gaps = list(reversed(sorted(gaps)))
    return sum(gaps[:2]) # take 2 tickets

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(x) for x in input().split(" ")]
        P = [int(x) for x in input().split(" ")]
        soln = solve(N, K, P)
        print (f"Case #{t}: {soln/K}")
