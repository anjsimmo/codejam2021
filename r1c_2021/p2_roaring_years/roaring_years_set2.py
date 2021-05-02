# Solves the Roaring Years problem by constructing candidate roaring years
# then taking the closest.
# Is fast enough to solve both Test Cases.

def construct(x, i):
    s = str(i)
    s_prev = s
    len_x = len(str(x))
    while len(s) <= len_x:
        i += 1
        s_prev = s
        s += str(i)
    # return both limited to len_x (lower bound), and one iter more (upper bound).
    return [int(s_prev), int(s)]

def construct_roaring(x):
    # x is the smallest (inclusive) number we are searching for.
    x_str = str(x)
    options = []
    for j in range(1,len(x_str)):
        i = int(x_str[:j])
        cs1 = construct(x, i)
        cs2 = construct(x, i+1)
        options += (cs1 + cs2)
    for jj in range(0,len(x_str)-1):
        i = int("1" + "0"*jj) # always consider starting from 1 (or 10, ...)
        cs3 = construct(x, i)
        options += cs3
    for jjj in range(1,len(x_str)-1):
        i = int("9"*jjj) # always consider wraps involving 9 (or 99, ...)
        for m in range(0, 18 + 2): # +2 not needed, but is defensive
            cs5 = construct(x, max(1, i - m))
            options += cs5
    for i in sorted(options):
        if i >= x:
            return i
    else:
        # e.g. for case of x = 1..9
        return 12

def solve(Y):
    return construct_roaring(Y+1)

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        Y  = int(input())
        soln = solve(Y)
        print (f"Case #{t}: {soln}")
