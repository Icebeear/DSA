class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", 
                    "]": "[", 
                    "}": "{"}
        stack = []
        for prent in s: 
            if prent not in hashmap: 
                stack.append(prent)
                continue
            elif not stack or stack[-1] != hashmap[prent]:
                return False 
            stack.pop()
        return not stack  
    
'''
https://leetcode.com/problems/valid-parentheses/description/
------------------------------------------------------------


'''