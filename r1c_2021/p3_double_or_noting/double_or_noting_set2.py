# Solves the Double or NOTing problem by construction.
# Is fast enough to solve both Test Cases.

def unslide(X):
    assert X[-1] == "0"
    return X[:-1]


def flip(X, drop_leading=True):
    flipped = "".join(["1" if x=="0" else "0" for x in X])
    if "1" in flipped:
        if drop_leading:
            return flipped[flipped.index("1"):]
        else:
            return flipped
    else:
        return "0"


def subsolve(E_tail):
    flips = 0
    
    while len(E_tail) > 0:
        if E_tail[-1] == "0":
            E_tail = unslide(E_tail)
            continue
        else:
            E_tail = flip(E_tail, drop_leading=False)
            flips += 1
    
    return flips


def solve(S, E):
    # returns (flips, slide) or (-1, -1) if impossible
    if S == E:
        return 0, 0
    if S == "0":
        # Only valid first move is to flip to a 1
        penalty_flips = 1
        S = "1"
    else:
        penalty_flips = 0
    flips = 0
    S_head = S
    while S_head != "0":
        if E.startswith(S_head):
            E_tail = E[len(S_head):]
            solve_flips = subsolve(E_tail)
            if solve_flips <= flips:
                # can construct tail in `solve_flips`. But still need at least `flips` to remove leading 1s, etc.
                # need to slide to construct E_tail
                slides = len(E_tail)
                return flips+penalty_flips, slides

        S_head = flip(S_head)
        flips += 1
    if E == "0":
        return flips+penalty_flips, 0
    else:
        solve_flips = subsolve(E)
        if solve_flips <= flips:
            slides = len(E)
            return flips+penalty_flips, slides
    return -1, -1


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        S, E  = input().split(" ")
        f, s = solve(S, E)
        soln = f + s # moves = flips + slides
        if soln < 0:
            print (f"Case #{t}: IMPOSSIBLE")
        else:
            print (f"Case #{t}: {soln}")
