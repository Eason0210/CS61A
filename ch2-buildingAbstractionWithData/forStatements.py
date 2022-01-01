"""Introduce For Statements"""
def count(s, value):
    """Count the number of times that value appear
    in sequence S.

    >>> count([1, 2, 1, 2, 1, 1], 1)
    4
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

## implement with while loop
# def count(s, value):
#     """Count the number of times that value appear
#     in sequence S.

#     """
#     total, index = 0, 0
#     while index < len(s):
#         element = s[index]
#         if element == value:
#             total = total + 1
#         index = index + 1

#     return total

# sequence unpacking in For statements
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]

same_count = 0
for x, y in pairs:
    if x == y:
        same_count += 1
print (same_count)
