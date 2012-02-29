# Ugly-prints unformatted 2d array.
def show(p):
    print p

# Returns range of indexes for given array.
def idx(arr):
    return range(len(arr))

# Creates x by y array of zeroes.
def z2d(x, y):
    return [[0]*x for i in range(0, y)]

# Uniform probability matrix given n positions.
def u2dn(x, y, positions):
    vu = 1.0 / len(positions)
    q = z2d(x, y)
    for x, y in positions:
        q[y][x] = vu
    return q

def u2d(x, y):
    p = 1.0 / (x * y)
    return [[p for i in range(0, x)] for j in range(0, y)]

def sum2d(p):
    return sum([sum(yarr) for yarr in p])

def N(p, s):
    return [n/s for n in p]

def N2d(p):
    ret = []
    total = sum2d(p)
    for yarr in p:
        ret.append(N(yarr, total))
    return ret

def S(p, c, U):
    q = []
    for i, w in enumerate(c):
        mult = sensor_right if U == c[i] else sensor_wrong
        q.append(p[i] * mult)
    return q

def S2d(p, U):
    q = []
    for i in idx(p):
        #pp(p[i])
        #pp(colors[i])
        q.append(S(p[i], colors[i], U))
    return N2d(q)

# Circular-world indices given array and x,y position.
# I'm not sure why I'm swapping here, or why 
def cidx_2d(a, x, y):
    ylen = len(a)
    xlen = len(a[0])
    return swap([x % xlen, y % ylen])

# Swaps two-element array values.
def swap(a):
    return [a[1], a[0]]

# 2d move.
def M2d(p, Z):
    q = z2d(len(p[0]), len(p))
    dy, dx = Z
    for y in idx(p):
        for x in idx(p[0]):
            pval = p[y][x]
            mult = p_move
            n = pval * mult
            qy, qx = cidx_2d(p, x+dx, y+dy)
            q[qy][qx] += n
            
            mult = p_move_wrong
            n = pval * mult
            qy, qx = cidx_2d(p, x, y)
            q[qy][qx] += n
    return N2d(q)

# Multiple move/sense in 2D.
def MS2d(p, Zs, Us):
    for i in idx(Zs):
        p = M2d(p, Zs[i])
        p = S2d(p, Us[i])
    return p

#
#
#

R, G = "red", "green"

colors = [[R, G, G, R, R],
          [R, R, G, R, R],
          [R, R, G, G, R],
          [R, R, R, R, R]]

measurements = [G, G, G, G, G]
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 0.8       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

p = u2d(5, 4)
p = MS2d(p, motions, measurements)
show(p)
