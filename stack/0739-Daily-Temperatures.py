class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = [] #pair: [t, day]
        for day, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                answer[stack[-1][1]] = day - stack[-1][1]
                stack.pop()
            stack.append([t, day])
        return answer 

'''
https://leetcode.com/problems/daily-temperatures/
-------------------------------------------------

'''        