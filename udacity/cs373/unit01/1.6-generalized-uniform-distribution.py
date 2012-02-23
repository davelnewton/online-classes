# Multiplying a single-element array creates 
# a 1-d array containing the original element.

# Initial code.
n = 5
p = [1.0 / n] * n

print p

# Returns a uniform probability array of size n.
def uniform_probability(n):
    return [1.0 / n] * n

print uniform_probability(10)
