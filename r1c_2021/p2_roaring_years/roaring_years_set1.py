# Solves the Roaring Years problem by incrementing year
# until we find one which is a roaring year.
# Solves Test Case 1, but times out on Test Case 2. 

def test_roaring_s(x, i):
    s = ""
    len_x = len(str(x))
    while len(s) < len_x:
        s += str(i)
        i += 1
    if str(x) == s:
        return True
    return False

def test_roaring(x):
    x_str = str(x)
    for j in range(1,len(x_str)):
        i = int(x_str[:j])
        if test_roaring_s(x, i):
            return True
    return False

def solve(Y):
    y = Y
    while True:
        y += 1
        if test_roaring(y):
            return y

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        Y  = int(input())
        soln = solve(Y)
        print (f"Case #{t}: {soln}")
