class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dictionary = defaultdict(list)

        for first,second in edges:
            dictionary[first].append(second)
            dictionary[second].append(first)

        def helper(node,viz):
            total = 0
            if node not in viz:
                viz.add(node)
            else:
                return total
            if hasApple[node]==True and node!=0:
                total += 2
            if len(dictionary[node])==0:
                return total
            for i in dictionary[node]:
                k = helper(i,viz)
                if i not in viz:
                    viz.add(i)
                if k>0:
                    total += k
                if hasApple[i]==False and k>0:
                    total += 2
            return total
        return helper(0,set())
