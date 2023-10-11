class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()

        ans = 0

        for i in range(len(edges)):
            if i in visited: continue

            count = 0
            memo = {}
            cur = i

            while cur != -1:
                if cur in memo:
                    ans = max(ans, count-memo[cur])
                    break
                if cur in visited: 
                    break

                memo[cur] = count
                visited.add(cur)
                count += 1
                cur = edges[cur]
            if ans >= len(edges)/2: break

        return ans if ans != 0 else -1
