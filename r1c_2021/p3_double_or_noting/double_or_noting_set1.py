# Solves the Double or NOTing problem by brute force.
# Solves Test Case 1, but Memory Limit Exceeded error on Test Case 2. 

def slide(X):
    if X == "0":
        return "0"
    return X + "0"


def flip(X):
    flipped = "".join(["1" if x=="0" else "0" for x in X])
    if "1" in flipped:
        return flipped[flipped.index("1"):]
    else:
        return "0"


def matches(a, b):
    if a == b:
        return True


def solve(S, E):
    moves = [S]
    moves2 = []
    total = 0
    while True:
        for move in moves:
            if matches(move, E):
                return total
            moves2.append(slide(move))
            moves2.append(flip(move))
        total += 1
        moves = moves2
        moves2 = []
        if total > max(2, len(S)) + len(E):
            break


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        S, E  = input().split(" ")
        soln = solve(S, E)
        if soln is None:
            print (f"Case #{t}: IMPOSSIBLE")
        else:
            print (f"Case #{t}: {soln}")
