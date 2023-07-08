class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t): 
           return False
       for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
       return True 

#O(n)
'''
https://leetcode.com/problems/valid-anagram/description/
--------------------------------------------------------
Если длина разная то сразу до связи, иначе чекаем в set(s) где только уникальные значения
если количество какой то из букв отличается то false 
'''