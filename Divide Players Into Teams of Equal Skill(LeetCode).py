class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        sorted_skill = sorted(skill)
        left = 0
        right = len(skill) - 1
        half = len(skill) // 2
        first_sum = sorted_skill[0]+sorted_skill[len(skill) - 1]
        sums = 0
        for i in range(half):
            while left < right:
                if sorted_skill[left]+sorted_skill[right] != first_sum:
                    return -1
                sums += sorted_skill[left]*sorted_skill[right]
                left += 1
                right -= 1
        return sums
