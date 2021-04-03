import numpy as np
import math

# Simulate dataset.
# For some reason, my initial algorithm scored highly on simulated
# data, but was marked wrong answer in CodeJam, so is possible that my
# simulator does not match Google's implementation.

P = 100
Q = 10000

def f(x):
    return 1 / (1 + math.exp(-x))

def gen_ps():
    ss = []
    for i in range(P):
        s = np.random.uniform(-3,3)
        ss.append(s)
    return ss

def gen_qs():
    qs = []
    for i in range(Q):
        q = np.random.uniform(-3,3)
        qs.append(q)
    return qs
    
def sim_single(s, q, cheat=False):
    if cheat:
        if np.random.random_sample() < 0.5:
            return 1
    p = f(s - q)
    result = 1 if np.random.random_sample() < p else 0
    return result

def sim_player(s, qs, cheat=False):
    results = [sim_single(s, q, cheat) for q in qs]
    return results

def sim_round(cheat_index=-1):
    ss = gen_ps()
    qs = gen_qs()
    rows = []
    for i in range(P):
        s = ss[i]
        row = sim_player(s, qs, i == cheat_index)
        rows.append(row)
    matrix = np.array(rows)
    return matrix

def print_matrix(matrix):
    return "\n".join(["".join([str(i) for i in row]) for row in matrix])
    
def generate(T):
    print(f"{T}")
    print("86")
    for i in range(T):
        matrix = sim_round(cheat_index=min(i, P)) # Cheater == Case number (or the last player for case 100 onward)
        print(print_matrix(matrix))

if __name__ == "__main__":
    generate(100)