class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        prev = float('-inf')
        answer = []
        for index, char in enumerate(s):
            if char == c:
                prev = index
            answer.append(index - prev)
        print(answer)

        prev = float('inf')
        for index in range(len(s) - 1, -1, -1):
            if s[index] == c:
                prev = index
            answer[index] = min(answer[index], prev - index)

        return answer
                
