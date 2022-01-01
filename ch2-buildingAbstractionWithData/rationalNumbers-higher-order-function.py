"""Rational Numbers such as 1/3 or 17/29,
implemented by higher-order functions."""

from math import gcd

# Rational arithmetic

def add_rationals(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), '/', denom(x))

# Constructor and selector

def rational(n, d):
    """Construct a rational number x that represents N/D"""
    g = gcd(n, d)
    def select(name):
        if name == 'n':
            return n//g
        elif name == 'd':
            return d//g
    return select

def numer(x):
    """Return the numerator of rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of rational number x."""
    return x('d')
