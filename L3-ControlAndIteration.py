'''CS61A Sommer 2020 Lecture 3: Control and Iteration'''
from operator import floordiv, mod

def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(2021, 10)
    >>> q
    202
    >>> r
    1
    """
    return floordiv(n, d), mod(n, d)

# $ python3 -m doctest -v L3-ControlAndIterator.py

# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,...

def fib(n):
    """Compute the nth Fibonacci number, for N >= 1."""
    pred, curr = 0, 1 # 0th and 1st Fibonacci numbers
    k = 1             # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr


# return statements
def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

# High order function
# 61A Spring 2018 Lecture 6 Video 3

# def search(f):
#     x = 0
#     while True:
#         if f(x):
#             return x
#         x += 1
def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)
