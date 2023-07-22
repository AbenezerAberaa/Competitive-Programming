class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dict_ = collections.defaultdict(list)
        for x, y in adjacentPairs:
            dict_[x].append(y)
            dict_[y].append(x)
            
        res = []
        for k, v in dict_.items():
            if len(v) == 1:
                res = [k, v[0]]
                break

        while len(res) < len(adjacentPairs)+1:
            for x in dict_[res[-1]]:
                if x != res[-2]:
                    res.append(x)
                    break
        
        return res
