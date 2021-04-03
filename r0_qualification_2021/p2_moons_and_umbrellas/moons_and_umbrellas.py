import math
import itertools


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


def toggle_generator():
    # CJCJCJCJ....
    while True:
        yield "C"
        yield "J"


def toggle_generator_n(n):
   return "".join(itertools.islice(toggle_generator(), n))


def fill_sec(a, length, c, X, Y):
    assert length > 0
    #print(f"TRACE: {a, length, c, X, Y}")
    if a == "C" and c == "C":
        if X + Y >= 0:
            # For every CJ, there must be a JC.
            # If the combined cost is positive, leave as CC...
            return "C" * length
        else:
            return toggle_generator_n(length)
    if a == "C" and c == "J":
        if X + Y >= 0:
            # For every additional CJ, there must be an additional JC.
            # If the combined cost is positive, leave as CC...J
            return "C" * length
        else:
            return toggle_generator_n(length)
    if a == "C" and c == "?":
        if X + Y < 0:
            # Combined cost of pairs is negative
            if length % 2 == 1:
                # Even number of elements
                if Y < 0 or length <= 1: # Bug fix: Can't modify if only 1 char.
                    return toggle_generator_n(length)
                else:
                    # Can save cost by not toggling the last pair:
                    # CJJ
                    return toggle_generator_n(length - 1) + "J"
            else:
                # Odd number of elements
                if X < 0 or length <= 1: # Bug fix: Can't modify if only 1 char. 
                    return toggle_generator_n(length)
                else:
                    # Can save cost by not toggling the last pair:
                    # CJCC
                    return toggle_generator_n(length - 1) + "C"
        else:
            if X < 0:
                # Value of CJ will not offset cost of JC
                return "C" + "J" * (length - 1)
            else:
                # Value of JC will not offset cost of CJ
                return "C" * length
    if a == "?" and c == "?":
        if X < Y:
            # CJ is more valuable (or less costly) => start with C
            return fill_sec("C", length, c, X, Y)
        else:
            return fill_sec("J", length, c, X, Y)
    if a == "?" and c != "?":
        # symetry
        #print(f"R1 TRACE: {a, length, c, X, Y}")
        # The last (first) letter shouldn't be returned, so drop this when reversing
        return reverse(fill_sec(c, length + 1, a, Y, X)[1:])
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
