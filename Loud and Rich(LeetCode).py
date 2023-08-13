class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        length = len(quiet)
        temp = [0]*length
        arr = [[] for i in range(length)]
        for i,j in richer:
            arr[i].append(j)
            temp[j] += 1
        result = [i for i in range(length)]
        value = [quiet[i] for i in range(length)]
        contain = []
        for i in range(length):
            if temp[i]==0:
                contain.append(i)
        while contain:
            x = contain.pop(0)
            for i in arr[x]:
                temp[i] -= 1
                if value[x] < value[i]:
                    result[i] = result[x]
                    value[i] = value[x]
                if temp[i] == 0:
                    contain.append(i)
        return result
