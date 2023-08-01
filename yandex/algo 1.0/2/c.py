lenght = int(input())
nums = list(map(int, input().split()))
n = int(input())

def f(nums, n): 
    diff = 10000 
    res = 0 
    for i in range(lenght):
        temp = abs(n - nums[i])
        if temp < diff:
            diff = temp
            res = nums[i]
    return res 

print(f(nums, n)) 