import math
import numpy as np 
import datetime

def f(x):
    return 1 / (1 + np.exp(-x))

f_min = f(-3)
f_max = f(3)
def f_inv(f):
    f = np.clip(f, f_min, f_max)
    return np.log(f) - np.log(1 - f)

def est_pr_q(score_col):
    return np.mean(score_col)

def est_pr_s(score_row):
    return np.mean(score_row)

def est_pr_qs(score_matrix):
    return np.apply_along_axis(est_pr_q, 0, score_matrix)

def est_pr_ss(score_matrix):
    return np.apply_along_axis(est_pr_s, 1, score_matrix)

def to_Q(pr):
    q = -f_inv(pr) # high pr => easy question
    return q
to_Q_vect = np.vectorize(to_Q)

def to_S(pr):
    s = f_inv(pr)
    return s
to_S_vect = np.vectorize(to_S)

def to_S_cheat(pr):
    cheat_pr = max(2 * pr - 1, 0)
    s = f_inv(cheat_pr)
    assert s > -3.1
    assert s < 3.1
    return s
to_S_cheat_vect = np.vectorize(to_S_cheat)

def est_log_pr(score_row, qs, s, cheat=False):
    # vectorized for speed
    obs = score_row
    q = qs
    pr_correct = f(s - q)
    if cheat:
        pr_correct = 0.5 + 0.5 * pr_correct
    pr_wrong = 1 - pr_correct
    log_pr = obs * np.log(pr_correct) + (1 - obs) * np.log(pr_wrong)
    return np.sum(log_pr)

def est_log_prs(score_matrix):
    pr_qs = est_pr_qs(score_matrix)
    pr_ss = est_pr_ss(score_matrix)
    qs = to_Q_vect(pr_qs)
    ss = to_S_vect(pr_ss)
    ss_cheat = to_S_cheat_vect(pr_ss)
    log_pr = [est_log_pr(row, qs, ss[i]) for i,row in enumerate(score_matrix)]
    log_pr_cheats = [est_log_pr(row, qs, ss_cheat[i], True) for i,row in enumerate(score_matrix)]
    return log_pr_cheats, log_pr

def solve(score_matrix):
    log_pr_cheats, log_pr = est_log_prs(score_matrix)
    log_pr_ratio = np.array(log_pr_cheats) - np.array(log_pr)
    cheat_index = np.argmax(log_pr_ratio) + 1
    return cheat_index

def parse_matrix(strs):
    score_rows = [[int(x) for x in row] for row in strs]
    score_matrix = np.array(score_rows)
    # 4000 columns is enough, too slow otherwise
    score_matrix = score_matrix[:,0:4000]
    return score_matrix

if __name__ == "__main__":
    T = int(input())
    P = int(input())
    N = 100
    for t in range(1, T + 1):
        buf = []
        for i in range(1, N + 1):
            buf.append(input())
        score_matrix = parse_matrix(buf)
        cheat = solve(score_matrix)
        print (f"Case #{t}: {cheat}")
