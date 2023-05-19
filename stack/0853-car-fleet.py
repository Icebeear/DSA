class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)

'''
https://leetcode.com/problems/car-fleet/description/
----------------------------------------------------
 

'''