n, k, m = map(int, input().split())
def details(n, k, m):
    details_per_bar = k // m 
    
    if details_per_bar == 0:
        return 0 
    
    res = 0 
    ost = k - (k // m) * m
    
    while n >= k:
        n -= k 
        res += details_per_bar
        n += ost
    return res 

print(details(n, k, m))


assert details(5, 2, 1) == 4
assert details(5, 3, 1) == 3
assert details(164, 5, 3) == 54
assert details(10, 5, 2) == 4
assert details(13, 5, 3) == 3
assert details(14, 5, 3) == 4
assert details(1, 1, 2) == 0    
assert details(1, 1, 1) == 1
assert details(200, 1, 1) == 200


