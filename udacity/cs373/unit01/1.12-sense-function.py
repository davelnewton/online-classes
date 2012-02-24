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

def sense(p, Z):
    q = []
    for i, w in enumerate(world):
        mult = pHit if Z == world[i] else pMiss
        q.append(p[i] * mult)
    return q

print p
print "Sum is %f" % sum(p)
print sense(p, Z)
