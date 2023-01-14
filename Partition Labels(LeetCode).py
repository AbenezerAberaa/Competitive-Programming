class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for index, char in enumerate(s):
            dic[char] = index
        
        maxu , size = 0, 1
        result = []
        for index, char in enumerate(s):
            maxu = max(maxu, dic[char])
            if index == maxu:
                result.append(size)
                size = 1
            else:
                size += 1
        return result


