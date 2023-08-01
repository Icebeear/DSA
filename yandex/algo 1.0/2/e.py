# n = int(input())
# nums = list(map(int, input().split()))

def f(nums):
    place = 1
    winner = max(nums)
    winner_index = nums.index(winner)
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] % 10 == 5 and nums[i + 1] < nums[i] and winner_index < i:
            for score in nums:
                if winner == score == nums[i]:
                    pass
                elif score > nums[i]:
                    place += 1  
            return place
    return 0
        
# print(f(n, nums))




assert f([10, 20, 15, 10, 30, 5, 1]) == 6
assert f([15, 15, 10]) == 1
assert f([10, 15, 20]) == 0
assert f([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5
assert f([1, 1, 1, 1, 5, 1]) == 0
assert f([100, 100, 100, 5, 4]) == 4
assert f([5, 1, 10, 20]) == 0 
assert f([1, 1, 1, 5]) == 0
assert f([100, 5, 100, 10]) == 0
assert f([100, 5, 4, 10]) == 3
assert f([4, 5, 1]) == 0
assert f([1000, 5, 1, 100, 200, 50]) == 5
assert f([10, 5, 1, 100, 200, 50]) == 0
assert f([5, 5, 4]) == 1
assert f([1, 1, 1, 1]) == 0
assert f([100, 5, 1]) == 2
assert f([5, 1]) == 0
assert f([20, 20, 20, 15, 1]) == 4
assert f([20, 20, 20, 10, 10, 10, 5, 1]) == 7




def g(throws):
    winner_throw = throws[0]
    winner_was_before = True
    vasya_best_throw = None
    for i in range(1, len(throws) - 1):
        throw = throws[i]
        if throw > winner_throw:
            winner_throw = throw
            winner_was_before = True
            vasya_best_throw = None
        else:
            if winner_was_before:
                if throw % 10 == 5 and throws[i + 1] < throw:
                    if not vasya_best_throw or vasya_best_throw < throw:
                        vasya_best_throw = throw

    if not vasya_best_throw:
        return 0

    vasya_best_placement = 1
    for throw in throws:
        if throw > vasya_best_throw:
            vasya_best_placement += 1

    return vasya_best_placement


assert g([10, 20, 15, 10, 30, 5, 1]) == 6
assert g([15, 15, 10]) == 1
assert g([10, 15, 20]) == 0
assert g([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5
assert g([1, 1, 1, 1, 5, 1]) == 0
assert g([100, 100, 100, 5, 4]) == 4
assert g([5, 1, 10, 20]) == 0 
assert g([1, 1, 1, 5]) == 0
assert g([100, 5, 100, 10]) == 0
assert g([100, 5, 4, 10]) == 3
assert g([4, 5, 1]) == 0
assert g([1000, 5, 1, 100, 200, 50]) == 5
assert g([10, 5, 1, 100, 200, 50]) == 0
assert g([5, 5, 4]) == 1
assert g([1, 1, 1, 1]) == 0
assert g([100, 5, 1]) == 2
assert g([0]) == 0
assert g([20, 20, 20, 15, 1]) == 4
assert g([20, 20, 20, 10, 10, 10, 5, 1]) == 7