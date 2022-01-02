"""Generator can yield form iterators."""

def a_then_b(a, b):
    """yield from statement yields all values from an iterator or iterable (Python 3.3).

    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    yield from a
    yield from b

# equivalent to below implement
    # for x in a:
    #     yield x
    # for x in b:
    #     yield x
