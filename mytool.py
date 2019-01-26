"""
 Some useful tools
"""

def file2list(n):
    arr = []
    for i in range(n):
        arr.append(input())
    return arr

def down_count(total):
    for i in range(200):
        n = float(input())
        total -= n
        print(total)
    return

def suitable_cube(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('input number must be a positive integer')
    x = int(pow(n, 0.5))
    upper_bound = x + 1
    y = x
    while x*y < n:
        if y < upper_bound:
            y += 1
        else:
            x += 1
    return x, y
