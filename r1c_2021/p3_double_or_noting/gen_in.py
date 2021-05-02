# Generate tests
R = 2**4 - 1
Q = 2**4 - 1
print((R+1)*(Q+1))
for i in range(0,R+1):
    for j in range(0,Q+1):
        print(f"{i:b} {j:b}")
