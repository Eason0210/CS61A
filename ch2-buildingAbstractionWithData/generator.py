"""Generators"""

def evens(start, end):
    """Evens is a generator.
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    >>> t = evens(2, 10)
    >>> next(t)
    2
    >>> next(t)
    4
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2
