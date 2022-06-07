# 200. Number of Islands
def numIslands(matrix):
    # Write your code here.
	if(not matrix):
            return 0
    count,R,C = 0,len(matrix), len(matrix[0])
        
    #Thinking is :
    #1. If encounter a 1, start a DFS and find all the connected component. This will represent an island
    #2. be careful to mark all the visted with an separate character to avoid duplicate count
    #3. Iterate through the matrix           
    def dfs(r,c):
        if(r<0 or r>R-1 or c<0 or c>C-1):
            return
        if(matrix[r][c]==1):
            matrix[r][c]=0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
                
    for r in range(R):
        for c in range(C):
            if(matrix[r][c]==1):
                dfs(r,c)
                count+=1
    return (count)


# DFS O(M*N) time | O(1) space

class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid)
                    islands += 1
        return islands 
    
    def dfs(self, r, c, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r + 1, c, grid)
