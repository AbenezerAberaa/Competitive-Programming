class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        maxu, inside =len(nums), [[nums[0]]]
        for i in range(1, maxu):
            insideThen = []
            for perm in inside:
                for j in range(0, i+1):
                    x=perm[:]
                    x.insert(j, nums[i])
                    insideThen.append(x)
            inside=insideThen
        return inside
