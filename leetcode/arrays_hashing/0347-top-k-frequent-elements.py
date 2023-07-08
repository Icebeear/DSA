class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1 
            else: 
                hashmap[x] = 1        
        sorted_tuple = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [sorted_tuple[i][0] for i in range(k)]
    
#O(nlogn)
'''
https://leetcode.com/problems/top-k-frequent-elements/description/
------------------------------------------------------------------
Дефолтный hashmap, ключ это число, value - сколько раз встречалось. 
Потом сортируем hashmap.items() по value с помощью lambda а не по ключам
ну и ретернем отсортированный уже 
'''