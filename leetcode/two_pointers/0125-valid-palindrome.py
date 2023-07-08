class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1 
            while l < r and not self.alphanum(s[r]):
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False 
            l += 1 
            r -= 1 
        return True 
            
    def alphanum(self, c):
        return ( 
            ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9")
        )
#O(n)
'''
https://leetcode.com/problems/valid-palindrome/description/
-----------------------------------------------------------
Идем левым указателем по строке пока не встретим буквку или цифру,
как только встретили идем правым указателем
a в финале сравниваем их, и если норм то идем дальше 
'''