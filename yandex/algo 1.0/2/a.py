nums = list(map(int, input().split()))

def f(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            return "NO"
    return "YES"


print(f(nums))