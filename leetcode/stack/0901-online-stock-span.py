class StockSpanner:

    def __init__(self):
        self.stack = [] # pair (price, span)

    def next(self, price: int) -> int:
        span = 1 
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1] 
            self.stack.pop()
        self.stack.append((price, span))
        return span 

'''
https://leetcode.com/problems/online-stock-span/description/
------------------------------------------------------------
храним пары, цена последняя и то сколько она съела перед собой чтобы перепрыгивать просто их 
'''