class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [day, t]
        for day, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                res[stack[-1][0]] = day - stack[-1][0]
                stack.pop()
            stack.append([day, t])
        return res

#O(n)
'''
https://leetcode.com/problems/daily-temperatures/
-------------------------------------------------
пока стек не пустой и t больше чем ласт элемент, в res меняем через сколько станет теплее и удаляем из стека
'''        