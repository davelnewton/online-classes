# Returns range of indexes for given array.
def idx(arr):
    return range(len(arr))

# Returns uniform probability array of size n.
def uniform_probability(n):
    return [1.0 / n] * n

pHit = 0.6
pMiss = 0.2
p = uniform_probability(5)
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']

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
