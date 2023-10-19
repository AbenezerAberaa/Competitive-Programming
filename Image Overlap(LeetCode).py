class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        image_1_index = [(i, j) for i, row in enumerate(img1) for j, num in enumerate(row) if num]
        image_2_index = [(i, j) for i, row in enumerate(img2) for j, num in enumerate(row) if num]
        indexCounter = collections.Counter((i - x, j - y) for i, j in image_1_index for x, y in image_2_index)
        return 0 if not indexCounter else max(indexCounter.values())
