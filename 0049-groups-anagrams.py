import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            key = [0] * 26 
            for letter in s: 
                key[ord(letter) - ord("a")] += 1 
            ans[tuple(key)].append(s)
        return ans.values()
'''
https://leetcode.com/problems/group-anagrams/description/
---------------------------------------------------------
ans - это словарь, у которого по умолчанию значения у ключей это пустые списки
потом мы проходимся по массиву, и для каждого слова создаем ключ, он выглядит вот так:
key = [0, 0, ...] 26 нулей там крч, каждый 0 это кол - во букв в слове
потом проходимся по слову, и для каждой буквы в key прибавлям сколько раз она встретилась.
Допустим для слова "adc" у нас будет ключ типа:
key = [1, 0, 1, 1, 0, 0....] то есть 1 буква а, 1 буква c и 1 буква d, и если в каком то еще слове
будет такое же количество букв, то ключит совпадут и мы заапендем туда еще и это слово.
Потом просто выводим ans.values()
ord дает букве ее ascii то есть ord(a) это 97
'''