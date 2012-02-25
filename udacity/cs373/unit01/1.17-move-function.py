# Returns range of indexes for given array.
def idx(arr):
    return range(len(arr))

# Returns uniform probability array of size n.
def uniform_probability(n):
    return [1.0 / n] * n

# Normalizes a probability array.
def normalize(arr):
    s = sum(arr)
    return [n/s for n in arr]

# Returns pHit if values the same, else pMiss.
def hit_or_miss(world_val, sense_val):
    return pHit if sense_val == world_val else pMiss

#
def sense(p, Z):
    return normalize([t[0] * hit_or_miss(t[1], Z) for t in zip(p, world)])

def sense_n(p, senses):
    for z in senses:
        p = sense(p, z)
    return p

# Rotates p left (U < 0) or right (U > 0) U places.
def rot_r(p):
    v = p.pop()
    return [v] + p

def rot_l(p):
    v = p.pop(0)
    return p + [v]

# Iteratively rotates list left/right.
def move1(p, U):
    for i in range(abs(U)):
        p = rot_r(p) if U > 0 else rot_l(p)
    return p

# Rotates left/right in one shot.
def move2(p, U):
    mult = -1 if U < 0 else 1
    mod = U % (len(p) * mult)
    if mod == 0:
        return p
    mod *= -1
    return p[mod:] + p[:mod]

# From course--may be easiest to read?
def move3(p, U):
    q = []
    for i in idx(p):
        q.append(p[(i-U) % len(p)])
    return q

pHit = 0.6
pMiss = 0.2

p = uniform_probability(5)
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
print sense_n(p, measurements)
