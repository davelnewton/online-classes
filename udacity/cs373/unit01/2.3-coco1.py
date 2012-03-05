def fx(n):
    n1 = n - 1
    taken = n1 / 5
    left = n1 - taken
    return [taken, left]

def f(n):
    return (n-1) / 5 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n

def is_int(n):
    return abs(n - int(n)) < 0.0000001

n = 1.
while not is_int(f6(n)):
    n += 1.

print x
