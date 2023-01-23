class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = Counter()
        print(dic)
        for winner, loser in matches:
            print(winner, loser)
            dic[loser] += 1
            dic[winner] += 0
        print(dic)
        result = [[],[]]
        for p in sorted(dic.keys()):
            if dic[p] == 0:
                result[0].append(p)
            if dic[p] == 1:
                result[1].append(p)
        return result
