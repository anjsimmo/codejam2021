import math

def normalise(z, w):
    if z == w:
        return 1, 1
    while True:
        d = math.gcd(z, w)
        if d <= 1:
            break
        z //= d
        w //= d       
    return z, w

def add_frac(a, b, c, d):
    # return e/f = a/b + c/d = (a*d + c*b) / b*d
    e = a * d + c * b
    f = b * d
    return normalise(e, f)

def score_q(As, actual):
    # calculate score vector based on participant As and actual answer.
    # score_q(("T", "T", "F"), "T") => (1, 1, 0)
    return tuple(1 if x==actual else 0 for x in As)

def add_score(s1, s2):
    # add two score vectors
    # add_score((10, 10, 10), (1, 0, 2)) => (11, 10, 12))
    return tuple(e1 + e2 for e1, e2 in zip(s1, s2))

def sub_score(s1, s2):
    # subtract two score vectors
    # sub_score((10, 10, 10), (1, 0, 2)) => (9, 10, 8))
    return tuple(e1 - e2 for e1, e2 in zip(s1, s2))

def inc(d, k, v):
    # d[k] += v, creating key if it does not exist
    if k not in d:
        d[k] = 0
    d[k] += v

def all_positive(s):
    # return True if all scores withing vector s are >= 0
    for x in s:
        if x < 0:
            return False
    return True

def bkcalc(fwdSP_map, As):
    # fwdSP_map: Forward Scores -> Forward Perms
    # As: Answers to this question
    bkSP_map = {}

    for s, p in fwdSP_map.items():
        s_q_true = score_q(As, "T")
        s_q_false = score_q(As, "F")
        bks_true = sub_score(s, s_q_true) # subtract because calculating backwards
        bks_false = sub_score(s, s_q_false)
        if all_positive(bks_true):
            inc(bkSP_map, bks_true, p)
        if all_positive(bks_false):
            inc(bkSP_map, bks_false, p)
    
    return bkSP_map

def fwdcalc(bkSP_map, As, fwdbkSP_map):
    fwdSP_map = {}
    perms_true = 0
    perms_false = 0
    for s, p in bkSP_map.items():
        s_q_true = score_q(As, "T")
        s_q_false = score_q(As, "F")
        fwds_true = add_score(s, s_q_true) # add
        fwds_false = add_score(s, s_q_false)
        if fwds_true in fwdbkSP_map: # Speed up: no point in tracking unreachable states
            inc(fwdSP_map, fwds_true, p)
        if fwds_false in fwdbkSP_map:
            inc(fwdSP_map, fwds_false, p)
        perms_true += p * fwdbkSP_map.get(fwds_true, 0)
        perms_false += p * fwdbkSP_map.get(fwds_false, 0)
    
    if perms_true >= perms_false:
         sel = "T"
         sel_perms = perms_true
    else:
         sel = "F"
         sel_perms = perms_false
    
    sel_perms_denom = perms_true + perms_false
    
    return fwdSP_map, sel, sel_perms, sel_perms_denom

def solve(N, Q, A, S):
    fwdSP_map = {tuple(S): 1}
    fwdbkSP_maps = [None] * Q # need to fill
    fwdbkSP_maps.append(fwdSP_map)
    
    # back calc
    for i in range(Q-1, 0, -1):
        # As is answers for this question
        As = [a[i] for a in A]
        bkSP_map = bkcalc(fwdSP_map, As)
        fwdbkSP_maps[i] = bkSP_map
        fwdSP_map = bkSP_map
    
    #print(fwdbkSP_maps)
    
    bkSP_map = {tuple([0]*N): 1}
    y = ""
    sel_perms_total, sel_perms_denom_total = (0, 1) # 0/1 = 0
    
    # forward calc
    for i in range(Q):
        As = [a[i] for a in A]
        fwdSP_map, sel, sel_perms, sel_perms_denom = fwdcalc(bkSP_map, As, fwdbkSP_maps[i+1])
        y += sel
        sel_perms_total, sel_perms_denom_total = add_frac(sel_perms_total, sel_perms_denom_total, sel_perms, sel_perms_denom)
        bkSP_map = fwdSP_map
    
    z, w = normalise(sel_perms_total, sel_perms_denom_total)
    return y, z, w

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, Q = [int(x) for x in input().split(" ")]
        A = []
        S = []
        for n in range(1, N + 1):
            a, s = input().split(" ")
            s = int(s)
            A.append(a)
            S.append(s)
        y, z, w = solve(N, Q, A, S)
        print(f"Case #{t}: {y} {z}/{w}")
