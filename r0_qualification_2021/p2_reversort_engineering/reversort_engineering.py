import math
import numpy as np 

def solve_old(L):
    # Solution to P1 (reversort)
    cost = 0
    for i in range(0, len(L)-1):
        j = i + np.argmin(np.array(L[i:])) + 1
        L = L[:i] + list(reversed(L[i:j])) + L[j:]
        cost += j-i
    return cost

def solve_algebraic(L, C):
    for i in range(0, len(L)-1):
        waste = min(C, len(L)-i-1)
        j = i + waste + 1
        L = L[:i] + list(reversed(L[i:j])) + L[j:]
        C -= waste
    return L

def solve(N, C):
    # 1. Apply Reversort algebraically to [a, b, c, ...]
    # 2. Attach numbers to final result [1, 2, 3, ...]
    # 3. Trace back to find numbers for a, b, c, ...
    C -= (N-1) # All ops have at least 1 unit cost
    if C < 0:
        return None
    L = solve_algebraic(list(range(N)), C)
    L_numbered = [(k, i+1) for i, k in enumerate(L)]
    L_sort = sorted(L_numbered)
    result = [v for (k, v) in L_sort]
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, C = [int(x) for x in input().split(" ")]
        soln = solve(N, C)
        if not soln:
            soln_str = "IMPOSSIBLE"
        else:
            actual_cost = cross_check = solve_old(soln) # cross-check
            if actual_cost != C:
                soln_str = "IMPOSSIBLE"
            else:
                soln_str= " ".join([str(x) for x in soln])
        print (f"Case #{t}: {soln_str}")
