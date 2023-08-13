class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        length = len(questions)
        results = [0] * (length + 1)
        for i in range(length-1, -1, -1):
            if i + questions[i][1] + 1 >= length + 1:
                next_one = 0
            else:
                next_one = results[i + questions[i][1] + 1]
            results[i] = max(questions[i][0] + next_one, results[i + 1])
        return results[0]
