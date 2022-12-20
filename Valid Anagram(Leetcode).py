class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = Counter(s)
        hash_map2 = Counter(t)
        sets = set(s)
        for each in sets:
            if each not in t or hash_map1[each] != hash_map2[each] or len(s) != len(t):
                return False
        return True
