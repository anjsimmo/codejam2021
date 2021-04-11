import math
import numpy as np 

def intlen(x):
    return len(str(x))

def increment(x_prev, x):
    x_prev = x_prev + 1 # must be at least 1 larger than previous
    if x >= x_prev:
        return x
    x_prev_str = str(x_prev)
    x_str = str(x)
    assert len(x_prev_str) >= len(x_str) # this is guaranteed if x_prev > x
    x_prev_str_start = x_prev_str[:len(x_str)]
    if x_str > x_prev_str_start:
        return int(x_str + "0" * (len(x_prev_str) - len(x_str)))
    if x_str < x_prev_str_start:
        return int(x_str + "0" * (1 + len(x_prev_str) - len(x_str)))
    assert x_str == x_prev_str_start 
    return x_prev

def solve(Xs):
    assert len(Xs) > 0
    total_cost = 0
    x_prev = 0
    for x in Xs:
        x_new = increment(x_prev, x)
        cost = intlen(x_new) - intlen(x)
        x_prev = x_new
        total_cost += cost
    return total_cost

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        Xs = [int(x) for x in input().split(" ")]
        soln = solve(Xs)
        print (f"Case #{t}: {soln}")
