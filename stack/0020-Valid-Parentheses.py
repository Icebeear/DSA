class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", 
                   "]": "[", 
                   "}": "{"}
        stack = []
        for prent in s:
            if not stack or (prent not in hashmap):
                stack.append(prent)
            elif hashmap[prent] == stack[-1]:
                stack.pop()
            else:
                return False 
            
        return len(stack) == 0
    
'''
https://leetcode.com/problems/valid-parentheses/description/
------------------------------------------------------------
если у нас пустой стек, или мы встречаем открывающуются скобку, то просто добавляет ее в стек 
а если у нас закрытая скобка, и он матчится по хешмапу с топом стека, то попаем и идем дальше
иначе ретернем false 
если все удалим, то true ретернем
'''