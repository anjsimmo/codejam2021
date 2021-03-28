import math
import numpy as np 

def solve(L):
    cost = 0
    for i in range(0, len(L)-1):
        j = i + np.argmin(np.array(L[i:])) + 1
        L = L[:i] + list(reversed(L[i:j])) + L[j:]
        cost += j-i
    return cost

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        L = [int(x) for x in input().split(" ")]
        soln = solve(L)
        print (f"Case #{t}: {soln}")
