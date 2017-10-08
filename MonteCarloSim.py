"""
This script is written for studying monte carlo simulation
in options pricing

"""

import matplotlib.pyplot as plt

def congruential_rng(x0, a, b, c, n):
    """ function to generate random number

    Args:
        x0(int)         : initial seed for rng
        a, b, c (int)   : params
        n (int)         : number of rng generated

    Returns:
        list of float
    """
    results = [x0]
    xi = x0
    for i in range(n):
        xi = (a * xi + b) % c
        u = xi / c
        results.append(u)
    return results

def congruential_rng2(seed, a, b, modulus):
    seed = (seed * a + b) % modulus
    yield seed
# recommended a,b,c is a = 7^5, b = 0, c = 2^31 - 1

a = 7**5
b = 0 
modulus = 2**31 -1
n = 10000
seed = 1
test = congruential_rng(seed, a, b, modulus, n)
test2 = congruential_rng2(seed, a, b, modulus)
result2 = [i for i in range(100)]
plt.hist(test)
plt.show()