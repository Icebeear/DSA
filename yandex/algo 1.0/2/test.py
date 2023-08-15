
# arr = [-1, -1, 0, 1, 1,]
# lst = list(arr) 
# lst_len = len(lst)

# pos_count, neg_count, zero_count  = 0, 0, 0

# for val in lst:
#     if val > 0:
#         pos_count += 1
#     elif val == 0:
#         zero_count += 1
#     elif val < 0:
#         neg_count += 1


# print(f"{(pos_count/lst_len):.6f}")        
# print(f"{(neg_count/lst_len):.6f}")        
# print(f"{(zero_count/lst_len):.6f}")      

# res = f"{(2 / 5):.6f}"  
# print(res)
# arr = [1, 2, 3, 4, 5]

# a = sum(arr) - max(arr)
# b = sum(arr) - min(arr)
# print(a, b)

# n = int(input())
# res = 0 
# for _ in range(n):
#     guys = list(map(int, input().split()))
#     if guys.count(1) >= 2:
#         res += 1 
# print(res)


# arr = list(map(int, input().split()))
# n = arr[0]
# k = arr[1]
# places = list(map(int, input().split()))
# place = places[k - 1] 
# res = 0 
# for x in places:
#     if x >= place and x > 0:
#         res += 1 
# print(res)

# arr = list(map(int, input().split()))
# m, n = arr[0], arr[1]
# print(m * n // 2)

# n = int(input())
# res = 0 
# for _ in range(n):
#     if input().replace("X", "") == "++":
#         res += 1 
#     else:
#         res -= 1 
# print(res)
from math import ceil 
arr = list(map(int, input().split()))
n, m, a = arr[0], arr[1], arr[2]

res = n * m / a ** 2 

if res < 1:
    print(1)
else:
    horizontal = ceil(n / a) 
    vertical = ceil(m / a) 
    print(horizontal * vertical)
    