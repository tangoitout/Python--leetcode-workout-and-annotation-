class Solution(object):
    def isToeplitzMatrix(self, matrix):
        kis=0
        for i in range((len(matrix))-1):
            for j in range((len(matrix[0]))-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    #matrix[i][j]!just means everything stack together
                    return False
        return True