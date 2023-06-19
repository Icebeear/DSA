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


#O(nlogn)
'''
https://leetcode.com/problems/car-fleet/description/
----------------------------------------------------
Добавляет в стек время за которое машина доедет до таргета, если в стеке 2 машины то чекаем, если та что машина взади
доедет за такое же время или быстрее то удаляем ее, как будто она объеденилась с машиной впереди и так далее
'''