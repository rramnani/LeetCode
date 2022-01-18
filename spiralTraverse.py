# Recursive: O(N) time, O(N) space, N = n*m => total no. of elements in the matrix
def spiralTraverse(array):
    # Write your code here.
	result = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
	print(result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
	if startRow > endRow or startCol > endCol:
		return
	
	for col in range(startCol, endCol + 1): # traverse the top border
		result.append(array[startRow][col])
	
	for row in range(startRow + 1, endRow + 1): # traverse the right border
		result.append(array[row][endCol])
	
	for col in reversed(range(startCol, endCol)): # traverse the bottom border
		if startRow == endRow:
			break
		result.append(array[endRow][col])
		
	for row in reversed(range(startRow + 1, endRow)): # traverse the left border
		if startCol == endCol:
			break
		result.append(array[row][startCol])
	
	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)
