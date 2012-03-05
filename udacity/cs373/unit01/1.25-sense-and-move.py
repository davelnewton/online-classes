# Returns uniform probability array of size n.
def uniform_probability(n):
    return [1.0 / n] * n

# Returns indices of array as range.
def idx(arr):
    return range(len(arr))

# Pretty-prints numeric array.
def pp(arr):
    for n in ["%1.6f" % n for n in arr]:
        print n,
    print

# (From class code)
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

# (From class code)
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

p = uniform_probability(5)
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]

p = uniform_probability(5)
pp(p)
for i in range(0, 2):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

pp(p)

