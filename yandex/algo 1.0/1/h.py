a, b, n, m = [int(input()) for _ in range(4)]

min_a = a * (n - 1) + n 
min_b = b * (m - 1) + m 

max_a = a * (n + 1) + n 
max_b = b * (m + 1) + m 

min_res = max(min_a, min_b)

max_res = min(max_a, max_b)

if min_res > max_res:
    print(-1)
else:
    print(" ".join(map(str, [min_res, max_res])))