import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrixcopy = copy.deepcopy(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrixcopy[row] = [0 for i in range(len(matrix[0]))]
                    for j in range(len(matrix)):
                        matrixcopy[j][col] = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrixcopy[row][col]