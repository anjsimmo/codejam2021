import math
import numpy as np 

def reverse(s):
    return s[::-1]

def eval_cost(X, Y, S):
    cost = 0
    state = ""
    for (a, b) in zip(S[:-1], S[1:]):
        if a == "C" and b == "J":
            cost += X
        elif a == "J" and b == "C":
            cost += Y
        
    return cost

toggle_map = {
    "C": "J",
    "J": "C",
    "?": "?"
}

def toggle(S):
    # "CCJ" -> "JJC"
    return "".join([toggle_map[x] for x in S])

def fill_sec(a, length, c, X, Y):
    #print(f"TRACE: {a, length, c, X, Y}")
    if a == "C" and c == "C":
        if X > 0 and Y > 0:
            return "C" * length
        else:
            raise Exception("Todo 1")
    if a == "C" and c == "J":
        if X > 0 and Y > 0:
            return "C" * length
        else:
            raise Exception("Todo 2")
    if a == "C" and c == "?":
        if X > 0 and Y > 0:
            return "C" * length
        else:
            raise Exception("Todo 3")
    if a == "?" and c == "?":
        if X > 0 and Y > 0:
            return "C" * length
        else:
            raise Exception("Todo 4")
    if a == "?" and c != "?":
        # symetry
        #print(f"R1 TRACE: {a, length, c, X, Y}")
        return reverse(fill_sec(c, length, a, Y, X))
    if a == "J":
        # symetry
        #print(f"R2 TRACE: {a, length, c, X, Y}")
        return toggle(fill_sec(toggle(a), length, toggle(c), Y, X))

    raise Exception("Uncovered case") # should never happen


def fill(X, Y, S):
    new_s = ""
    i = 0
    j = 1
    while True:
        if j >= len(S):
            new_s += fill_sec(S[i], j - i, "?", X, Y)
            break
        if S[j] == "?":
            j += 1
            continue
        if S[j] != "?":
            new_s += fill_sec(S[i], j - i, S[j], X, Y)
            i = j
            j += 1
            continue
        raise Exception("Uncovered case") # should never happen
    return new_s

def solve(X, Y, S):
    #print(S)
    filled = fill(X, Y, S)
    #print(filled)
    cost = eval_cost(X, Y, filled)
    #print(cost)
    return cost

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        X, Y, S = input().split(" ")
        X = int(X)
        Y = int(Y)
        soln = solve(X, Y, S)
        print (f"Case #{t}: {soln}")
