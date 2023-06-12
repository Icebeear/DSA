class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            if (target - v) in hashmap:
                return [hashmap[target - v], i]
            hashmap[v] = i  
#O(n)
'''
https://leetcode.com/problems/two-sum/
--------------------------------------
Юзаем хешмап, через enumerate итерируемся и если target - число в хешмапе, то ретернем
hashmap с ключом taget - v и i, иначе в hashmap добавляем ключ - число, value ключа это индекс 
'''