# Formats a 2D array, spacing floats and strings the same.
def fmt(x):
    f = "%s"
    if (type(x) == float) or (type(x) == int):
        f = "%01.04f"
    elif (type(x) == str):
        f = "%6s"
    return f

# Pretty-prints an array row.
def pp(arr):
    for s in [fmt(x) % x for x in arr]:
        print s,
    print

# Pretty-prints a 2D array.
def pp2d(arrs):
    for yarr in arrs:
        pp(yarr)

# Returns range of indexes for given array.
def idx(arr):
    return range(len(arr))

# Creates x by y array of zeroes.
def z2d(x, y):
    return [[0]*x for i in range(0, y)]

# Creates x by y array with incrementing n in each cell; for testing.
def n2d(x, y):
    q = z2d(x, y)
    n = 0
    for i in range(0, y):
        for j in range(0, x):
            q[i][j] = n
            n += 1
    return q
            
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

def cidx_2d(a, x, y):
    ylen = len(a)
    xlen = len(a[0])
    return [x % xlen, y % ylen]

# Or itertools.permutations([-1, 0, 1], 2)
def offsets():
    q = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            q.append([i, j])
    return q

def xM2d(p, Z):
    dy, dx = Z # [0, 1] is "move 1 right", dy=0, dx=1
    q = z2d(len(p[0]), len(p))
    for y in idx(p):
        for x in idx(p[y]):
            pval = p[y][x]
            print "p(x=%d, y=%d) = %1.4f" % (x, y, pval)
            for ox, oy in offsets():
                #if not ((abs(ox) == 1) and (abs(oy) == 1)):
                mult = p_move if ((ox == 0) and (oy == 0)) else p_move_wrong
                mpval = pval * mult
                print "  (ox=%2d, oy=%2d)" % (ox, oy)
                print "    pval=%1.4f x mult=%1.2f = %1.4f (mpval)" % (pval, mult, mpval)
                cdx, cdy = cidx_2d(p, ox+dx, oy+dy)
                print "    q(cdx=%2d, cdy=%2d)+=%1.4f (%1.4f+%1.4f)" % (cdx, cdy, mpval, q[cdy][cdx], mpval)
                q[cdy][cdx] += mpval
            pp2d(q) if x != idx(p[y])[-1:][0] else False
        pp2d(q) if y != idx(p)[-1:][0] else False
    pp2d(q)
    return N2d(q)

def xx_offsets(dx, dy):
    q = []
    #if (dx == 0) and (dy == 0):
    #    return q
    
    xoffs = [-1, 0, 1] if abs(dx) == 1 else [0]
    yoffs = [-1, 0, 1] if abs(dy) == 1 else [0]
    for dx in xoffs:
        for dy in yoffs:
            q.append([dx, dy])
    return q
            
def xxM2d(p, Z):
    dy, dx = Z # [0, 1] is "move 1 right", dy=0, dx=1
    q = z2d(len(p[0]), len(p))
    for y in idx(p):
        for x in idx(p[y]):
            pval = p[y][x]
            print "p(x=%d, y=%d) = %1.4f" % (x, y, pval)
            for oy, ox in offsets():#xx_offsets(dx, dy):
                #if not ((abs(ox) == 1) and (abs(oy) == 1)):
                mult = p_move if ((ox == 0) and (oy == 0)) else p_move_wrong
                mpval = pval * mult
                print "  (ox=%2d, oy=%2d)" % (ox, oy)
                print "    pval=%1.4f x mult=%1.2f = %1.4f (mpval)" % (pval, mult, mpval)
                cdx, cdy = cidx_2d(p, x+ox+dx, x+oy+dy)
                print "    q(cdx=%2d, cdy=%2d)+=%1.4f (%1.4f+%1.4f)" % (cdx, cdy, mpval, q[cdy][cdx], mpval)
                q[cdy][cdx] += mpval
            pp2d(q) if x != idx(p[y])[-1:][0] else False
        pp2d(q) if y != idx(p)[-1:][0] else False
    pp2d(q)
    return N2d(q)
                

# xM2d(pn, [0, 1])

def swap(a):
    return [a[1], a[0]]

# Z will be array/tuple (x, y).
def M2d(p, Z):
    q = z2d(len(p[0]), len(p))
    dy, dx = Z
    for y in idx(p):
        for x in idx(y):
            pval = p[y][x]
            print x, ",", y, "=", pval
            for oy, ox in offsets():
                print "  ox, oy=", ox, ",", oy
                mult = p_move if ((ox == 0) and (oy == 0)) else p_move_wrong
                n = pval * mult
                print "   ", cidx_2d(p, x+ox, y+oy), "=", n
                qx, qy = cidx_2d(p, x+dx+ox, y+dy+oy)
                print "   ", qx, ",", qy, "+=", n
                q[qy][qx] += n
    pp2d(q)
    return N2d(q)

#
#
#

R, G = "red", "green"
measurements = [R, G]
motions = [[0, 0], [0, 1]]

sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

#
# Test 1
#
sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

colors = [[G, G, G],
          [G, R, G],
          [G, G, G]]
pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1 = M2d(p, [0, 0])
pp2d(p1)
p2 = S2d(p1, R)
pp2d(p2)

#
# Test 2
#

colors = [[G, G, G],
          [G, R, R],
          [G, G, G]]
pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1 = M2d(p, [0, 0])
pp2d(p1)
p2 = S2d(p1, R)
pp2d(p2)

#
# Test 3
#

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)

#
# Test 4
#

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)
p = p1s

p2m = M2d(p, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
# Test 5
#

sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)
p = p1s

p2m = M2d(p, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
# Test 6
#

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)

p2m = xM2d(p1s, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
#
#

#
#
#

#
#
#

#
#
#

#
#
#

#p = u2d(3, 3)
#pp2d(p)

#pp2d(s2d(p, R))

#M2d(p, [1, 0])
