import math
import numpy as np


def safeget(L, i, d):
    try:
        return L[i]
    except IndexError:
        return d


def sim(Y, A, B, U):
    M = [0] * (Y - 1) + [1]
    for i in range(Y-1, -1, -1):
        if M[i] > safeget(U, i, 0):
            diff = M[i] - safeget(U, i, 0)
            # Greedily destroy any excess blocks at U[i]
            # to create more materials 
            M[i] -= diff
            if i - A >= 0:
                M[i - A] += diff
            if i - B >= 0:
                M[i - B] += diff
    return M


def solve(N, A, B, U):
    # worst case, A = 19, B = 20, => doubles at 19 * 20.
    # worst case, 20 * 20 blocks (achievable in 9 doublings) needed at 20th element
    # this will be enough to supply everything downstream
    Y_UPPER_BOUND = math.ceil(math.log2(sum(U))) * np.lcm(A,B) + len(U)
    
    for Y in range(1,Y_UPPER_BOUND+1):
        M = sim(Y, A, B, U)
        if M[:len(U)] == U:
            return Y


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, A, B = [int(x) for x in input().split(" ")]
        U = [int(x) for x in input().split(" ")]
        y = solve(N, A, B, U)
        if y is None:
            print (f"Case #{t}: IMPOSSIBLE")
        else:
            print (f"Case #{t}: {y}")
