class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        my_dict = Counter()
        for num in arr:
            my_dict[num + difference] = my_dict[num] + 1 if num in my_dict else 1

        return max(my_dict.values())  
