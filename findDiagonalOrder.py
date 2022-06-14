# 498. Diagonal Traverse

# O(M* N) time | 

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows_length = len(mat)
        cols_length = len(mat[0])

        result = []

        row, col = 0, 0

        for i in range(rows_length * cols_length):
            result.append(mat[row][col])

            if (row + col) % 2 == 0: # will go up
                if col == cols_length - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else: # will go down
                if row == rows_length - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result
        

    
            
def main():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    res = solution.findDiagonalOrder(mat)
    print(res)

if __name__ == "__main__": 
    main()
