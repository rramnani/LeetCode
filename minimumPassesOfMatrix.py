# Solution using 2 queues
# O(W*H) time, W-> width of matrix, H -> height of the matrix
# O(W*H) space
def minimumPassesOfMatrix(matrix):
	passes = convertNegatives(matrix)
  return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
	nextPassQueue = getAllPositivePositions(matrix)
	print(nextPassQueue)
	passes = 0
	
	while len(nextPassQueue) > 0:
		currentPassQueue = nextPassQueue
		nextPassQueue = []
		
		while len(currentPassQueue) > 0:
			row, col = currentPassQueue.pop(0) # O(N) operation
			positions = getNeighbors(row, col, matrix)
			
			for position in positions: # neighbors of current element
				row, col = position
				value = matrix[row][col]
				
				if value < 0:
					matrix[row][col] = value * -1
					nextPassQueue.append([row, col])
		passes += 1
	
	return passes

def getNeighbors(i, j, matrix): # get me a list of valid neighbors for the current element I'm it (i, j)
	neighbors = []
	if j < len(matrix[0]) - 1:
		neighbors.append([i, j + 1])
	if i < len(matrix) - 1:
		neighbors.append([i + 1, j])
	if j > 0:
		neighbors.append([i, j - 1])
	if i > 0:
		neighbors.append([i - 1, j])
	return neighbors	
	
def getAllPositivePositions(matrix): # O(W*H) time
	positivePositions = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] > 0: 
				positivePositions.append([i, j])
	return positivePositions

def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False
