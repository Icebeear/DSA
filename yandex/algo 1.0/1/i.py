a, b, c, d, e = [int(input()) for _ in range(5)]

def prisoner(a, b, c, d, e):
    breaks = sorted([a, b, c])
    holes = sorted([d, e])
    return "YES" if (breaks[0] <= holes[0] and breaks[1] <= holes[1]) else "NO"

print(prisoner(a, b, c, d, e))

assert prisoner(1, 1, 1, 1, 1) == 'YES'
assert prisoner(2, 2, 2, 1, 1) == 'NO'
assert prisoner(2, 2, 1, 1, 1) == 'NO'
assert prisoner(2, 1, 2, 1, 1) == 'NO'
assert prisoner(2, 1, 1, 1, 1) == 'YES'
assert prisoner(3, 8, 5, 5, 2) == 'NO'
assert prisoner(100, 1, 1, 5, 2) == 'YES'
assert prisoner(1, 1, 1, 5, 2) == 'YES'
assert prisoner(2, 8, 5, 5, 2) == 'YES'
