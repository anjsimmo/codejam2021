
def find_pos(known, min_pos, max_pos, k):
    assert max_pos >= min_pos
    n = max_pos - min_pos + 1
    if n == 1:
        assert min_pos == max_pos
        return min_pos
    if n == 2:
        # Needlessly expand search range to ensure our query only consists of distinct elements.
        if min_pos > 0:
            min_pos = min_pos - 1
            n = 3
        elif max_pos < len(known):
            max_pos = max_pos + 1
            n = 3
        else:
            assert len(known) == 1
            assert min_pos == 0
            assert max_pos == 1
            # case where we only have one known element and need to sort the other one.
            # either position (0 or 1) is acceptable, as can't determine order using medians.
            return 1
    bucket_size = n//3
    off_i = min_pos + bucket_size
    off_k = min_pos + bucket_size*2
    i = known[off_i - 1]
    j = known[off_k - 1]
    print(f"{i} {j} {k}")
    result = int(input())
    if result == -1:
        raise Exception("Out of moves")
    if result == i:
        return find_pos(known, min_pos, off_i - 1, k)
    if result == k:
        return find_pos(known, off_i, off_k - 1, k)
    if result == j:
        return find_pos(known, off_k, max_pos, k)
    raise Exception("Unexpected response")


def solve(N, Q):
    known = []
    for k in range(1, N+1):
        pos = find_pos(known, 0, len(known), k)
        known.insert(pos, k)
    return known


if __name__ == "__main__":
    T, N, Q = [int(x) for x in input().split(" ")]
    for t in range(1, T + 1):
        soln = solve(N, Q)
        print(" ".join([str(x) for x in soln]))
        correct = int(input())
        if correct == -1:
            raise Exception("Wrong Answer")
        if correct != 1:
            raise Exception("Unexpected judging result")