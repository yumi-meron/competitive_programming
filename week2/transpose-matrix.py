class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = [[0]*len(matrix) for clm in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transposed[j][i] = matrix[i][j]
        return transposed

            
        