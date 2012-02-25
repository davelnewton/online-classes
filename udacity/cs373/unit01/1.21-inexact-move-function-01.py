def idx(arr):
    return range(len(arr))

def cidx(arr, idx):
    return idx % len(arr)

def inexact_move1(p, M, errs):
    l = len(p)
    q = [0] * l
    for i in idx(p):
        for offset in [n-1 for n in idx(errs)]:
            q[(i + M + offset) % l] += p[i] * errs[offset+1]
    return q

class CArray(list):
    def __getitem__(self, index):
        return list.__getitem__(self, index % len(self))
    def __setitem__(self, index, value):
        return list.__setitem__(self, index % len(self), value)

def inexact_move2(p, M, errs):
    l = len(p)
    q = CArray([0] * l)
    for i in idx(p):
        for offset in [n-1 for n in idx(errs)]:
            q[i + M + offset] += p[i] * errs[offset+1]
    return q

errs = [0.1, 0.8, 0.1]

p1 = [0, 1, 0, 0, 0]
print inexact_move1(p1, 2, errs)

p2 = [0, 0.5, 0, 0.5, 0]
print inexact_move1(p2, 2, errs)

p3 = [.2, .2, .2, .2, .2]
print inexact_move1(p3, 2, errs)

p1 = [0, 1, 0, 0, 0]
print inexact_move2(p1, 2, errs)

p2 = [0, 0.5, 0, 0.5, 0]
print inexact_move2(p2, 2, errs)

p3 = [.2, .2, .2, .2, .2]
print inexact_move2(p3, 2, errs)

def pp(arr):
    for n in ["%1.6f" % n for n in arr]:
        print n,
    print
    
p = [1, 0, 0, 0, 0]
pp(p)
for x in range(0, 100):
    p = inexact_move2(p, 1, errs)
    pp(p)

