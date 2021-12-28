# O(N) time, O(1) space
def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) - 1 
	while i<j:
		print(array, i, j)
		if array[j] == toMove:
			j -= 1
		if array[i] == toMove: # and we have found the candidate at the end of array to move to beginnning: array[j] != toMove
			array[i], array[j] = array[j], array[i]
		if array[i] != toMove:
			i += 1
	return array
