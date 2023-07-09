a = int(input())
b = int(input())
c = int(input())

def f(a, b, c):
    if c < 0:
        return "NO SOLUTION"

    if a == 0:
        if c ** 2 == b:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"

    x = (c ** 2 - b) / a 

    if x.is_integer():
        return int(x) 
    
    return "NO SOLUTION"

print(f(a,b,c))

assert f(0, 0, 0) == 'MANY SOLUTIONS'
assert f(1, 0, 0) == 0
assert f(1, 2, 3) == 7
assert f(3, 13, 7) == 12
assert f(0, 0, 5) == 'NO SOLUTION'
assert f(0, 4, 2) == 'MANY SOLUTIONS'
assert f(0, 2, 2) == 'NO SOLUTION'
assert f(1, 2, -3) == 'NO SOLUTION'
assert f(2, 2, 3) == 'NO SOLUTION'


