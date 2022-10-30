class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        MOD = 10**9 + 7
        container = Counter(arr)
        for x in container:
            for y in container:
                if x > y:
                    continue
                z = target - x - y
                if y <= z and z in container:
                    if x == y == z:
                        count += container[x] * (container[x] - 1) * (container[x] - 2) // 6
                    elif x == y:
                        count += container[x] * (container[x] - 1) * container[z] // 2
                    elif x == z:
                        count += container[x] * (container[x] - 1) * container[y] // 2
                    elif y == z:
                        count += container[x] * container[y] * (container[y] - 1) // 2
                    else:
                        count += container[x] * container[y] * container[z]
        return count % MOD
        