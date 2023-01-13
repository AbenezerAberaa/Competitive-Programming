class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        for index, temp_val in enumerate(temperatures):
            while stack and temp_val > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = (index - stackIndex)
            stack.append([temp_val, index])
        return answer
