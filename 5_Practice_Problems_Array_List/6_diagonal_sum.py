# Given a square matrix mat, return the sum of the 
# matrix diagonals.
# Only include the sum of all the elements on the 
# primary diagonal and all the elements on the secondary
# diagonal that are not part of the primary diagonal.

def diagonalSum( mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        oppo_j = len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j :
                    sum += mat[i][j]
                elif j == oppo_j :
                    sum += mat[i][j]
            oppo_j -= 1
        return sum

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))