a1, b1, a2, b2 = map(int, input().split())

combinations = [ 
	(a1 + a2, max(b1, b2)),
	(a1 + b2, max(b1, a2)),
	(max(a1, a2), b1 + b2),
	(max(a1, b2), b1 + a2),
]

res = min(combinations, key=lambda x: x[0] * x[1])
print(res[0], res[1])