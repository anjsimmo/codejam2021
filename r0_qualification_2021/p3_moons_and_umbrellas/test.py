from moons_and_umbrellas import *

def S_perms(length):
    if length == 0:
        yield ""
        return
    x = length - 1
    for p in S_perms(x):
        yield "C" + p
    for p in S_perms(x):
        yield "J" + p

def mask_perms(S, length):
    if length <= 0:
        yield ""
        return
    for p in mask_perms(S[1:], length - 1):
        yield S[0] + p
        yield "?" + p

cost_perms = [
  (0, -1),
  (0, 0),
  (0, 1),
  (1, -20),
  (1, -3),
  (1, -2),
  (1, -1),
  (1, 0),  
  (1, 1),
  (1, 2),
  (1, 3),
  (1, 20),
  (2, -20),
  (2, -5),
  (2, -4),
  (2, -3),
  (2, -2),
  (2, -1),
  (2, 0),
  (2, 1),
  (2, 2),
  (2, 3),
  (2, 4),
  (2, 20),
  (-1, -20),
  (-1, -3),
  (-1, -2),
  (-1, -1),
  (-1, 0),  
  (-1, 1),
  (-1, 2),
  (-1, 3),
  (-1, 20),
  (-2, -20),
  (-2, -5),
  (-2, -4),
  (-2, -3),
  (-2, -2),
  (-2, -1),
  (-2, 0),
  (-2, 1),
  (-2, 2),
  (-2, 3),
  (-2, 4),
  (-2, 20)
]

# as an extra measure, also add all flipped pairs of cost permuntations
cost_perms += [(j, i) for i, j in cost_perms]

def test_valid(S_masked, S):
    # check that S only modifies "?" character, not the rest of the string.
    # e.g. CCC is not a valid solution to CJ?
    if len(S_masked) != len(S):
        return False
    for a, b in zip(S_masked, S):
        if a != "?" and a != b:
            return False
    return True

def do_test(L):
    print(f"Begin tests of perms up to length {L}")
    for S in S_perms(L):
        for S_masked in mask_perms(S, L):
            for X, Y in cost_perms:
                #continue
                actual_cost = eval_cost(X, Y, S)
                solved_cost = solve(X, Y, S_masked)
                filled = fill(X, Y, S_masked)
                
                if not test_valid(S_masked, filled):
                    print(f"BAD MASK: {X}, {Y}, {S_masked}. Actual: {S} {actual_cost}. Solved: {filled} {solved_cost}")
                elif solved_cost > actual_cost:
                    print(f"BAD COST: {X}, {Y}, {S_masked}. Actual: {S} {actual_cost}. Solved: {filled} {solved_cost}") 
                else:
                    #print(f"PASS: {X}, {Y}, {S_masked}. Actual: {S} {actual_cost}. Solved: {filled} {solved_cost}")
                    pass
    print("End of tests")

if __name__ == "__main__":
    for L in range(1,6+1):
        do_test(L)