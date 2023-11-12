class Solution:
    def leastBricks(self, wall) -> int:
        hashmap = {0 : 0}
        for row in wall:
            total = 0 
            for brick in row[:-1]:
                total += brick
                hashmap[total] = 1 + hashmap.get(total, 0) 

        return len(wall) - max(hashmap.values())

'''
https://leetcode.com/problems/brick-wall/description/
-----------------------------------------------------
считаем количество пропусков между кирпичами по каждму индексу и потом из длины стены
вычитаем максимальное количество которое получилось 
'''