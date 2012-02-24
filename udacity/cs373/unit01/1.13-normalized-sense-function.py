def uniform_probability(n):
    return [1.0 / n] * n

def m_mult(m1, m2):
    ret = []
    for i, n in enumerate(m1):
        ret.append(n * m2[i])
    return ret

def m_sum(m):
    sum = 0
    for n in m:
        sum += n
    return sum


pHit = 0.6
pMiss = 0.2
p = uniform_probability(5)
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'

def idx(arr):
    return range(len(arr))

def m_normalize(arr):
    s = sum(arr)
    return [n/s for n in arr]

def sense(p, Z):
    q = []
    for i, w in enumerate(world):
        mult = pHit if Z == world[i] else pMiss
        q.append(p[i] * mult)
    
    return m_normalize(q)    

def sense2(p, Z):
    q = []
    ts = zip(p, world)
    for t in ts:
        mult = (pHit if Z == t[1] else pMiss)
        q.append(t[0] * mult)
    return m_normalize(q)

def sense3(p, Z):
    ts = zip(p, world)
    return m_normalize([t[0] * (pHit if Z == t[1] else pMiss) for t in ts])

def sense4(p, Z):
    return m_normalize([t[0] * (pHit if Z == t[1] else pMiss) for t in zip(p, world)])

print p
print "Sum is %f" % sum(p)
print sense(p, Z)
