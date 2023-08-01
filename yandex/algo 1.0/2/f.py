input()
nums = list(map(int, input().split()))

def is_symmetrical(nums):
    return (nums == nums[::-1])

def f(nums):
    if is_symmetrical(nums):
        return 0

    res = []
    for _ in range(len(nums)):
        if not is_symmetrical(nums):
            res.append(nums[0])
            nums.pop(0)
        else:
            res = [str(num) for num in res]
            return f"{len(res)}\n{' '.join(res[::-1])}"
        
print(f(nums))

'''
удаляем 1 элемент из nums пока nums не станет семметричным и добавляем его в res
потом ретенем реверснутый res
'''
    