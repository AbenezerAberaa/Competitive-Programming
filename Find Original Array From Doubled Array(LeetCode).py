class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        res = []
        
        hashes = Counter()
        for value in changed:
            if value % 2 == 0  and value // 2 in hashes and hashes[value // 2] > 0:
                res.append(value // 2)
                hashes[value // 2] -= 1
            else:
                hashes[value] += 1
        if len(res) * 2 != len(changed):
            return []
        return res
        
