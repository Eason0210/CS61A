"""How to use Assertions:
what happens if you run half_fact(5)?"""

def fact(x):
    # assert isinstance(x, int)
    # assert x >= 0
    print("Debug: x= ", x) # print debugging

    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

def half_fact(x):
    return fact(x / 2)
