class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        hash_table = {}
        for i in logs:
            for b_d in range(i[0],i[1]):
                if b_d not in hash_table:
                    hash_table[b_d] = 1
                else:
                    hash_table[b_d] += 1
        result = []
        for i in hash_table:
            if hash_table[i]==max(hash_table.values()):
                result.append(i)
        return min(result)
        