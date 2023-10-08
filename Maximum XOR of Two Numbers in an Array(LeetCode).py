class Trie:
    def __init__(self,k):
        self.dict1 = {}
        self.size = k

    def insert(self,num):
        dict2 = self.dict1

        for i in range(self.size,-1,-1):
            bit = bool(num&(1<<i))
            if bit not in dict2:
                dict2[bit] = {}

            dict2 = dict2[bit]

    def find_max(self, num):
        dict2 = self.dict1
        xor = 0

        for i in range(self.size,-1,-1):
            bit = bool(num&(1<<i))
            if (1-bit) in dict2:
                xor |= (1<<i)
                dict2 = dict2[1-bit]
            else:
                dict2 = dict2[bit]

        return xor

class Solution:
    def findMaximumXOR(self, nums):
        k = len(bin(max(nums))[2:])

        trie = Trie(k)

        for i in nums:
            trie.insert(i)

        xor = 0

        for i in nums:
            xor = max(xor, trie.find_max(i))

        return xor
