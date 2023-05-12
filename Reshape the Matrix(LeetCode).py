class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        org_rows = len(mat)
        org_cols = len(mat[0])
        org_pro = org_rows * org_cols
        new_pro = r * c
        

        if org_pro != new_pro:
            return mat
        else:
            new_mat = []
            for index in range(r):
                new_mat.append([0]*c)
            for x in range(org_rows):
                for y in range(org_cols):
                    num = x * org_cols + y
                    new_mat[num//c][num%c] = mat[x][y]
            
            return new_mat
