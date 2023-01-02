class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sub_sum = sum(arr[:k])
        if curr_sub_sum // k >= threshold:
            count = 1
        else:
            count = 0
        for index in range(1, len(arr)-k+1):
            curr_sub_sum -= arr[index-1]
            curr_sub_sum += arr[index + k-1]
            if (curr_sub_sum) >= k*threshold:
                count += 1
        return count









