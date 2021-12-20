# O(N^2): Worst case time complexity, O(logN) space 
# O(N*logN): AVG. case time complexity
# every call of quickSortHelper takes ~ O(N) time (dividing array into smaller subarrays)
def quickSort(array):
	# Write your code here.
	quickSortHelper(array, 0, len(array)-1)
    return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx<endIdx:
		pIdx = partitionIndex(array, startIdx, endIdx)	
		quickSortHelper(array, startIdx, pIdx-1)
		quickSortHelper(array, pIdx+1, endIdx)
		
def partitionIndex(array, startIdx, endIdx):
	pivot = array[endIdx] #choosing the last idx to be the pivot
	partitionIdx = startIdx
	for j in range(startIdx, endIdx):
		if array[j] < pivot:
			array[j], array[partitionIdx] = array[partitionIdx], array[j]
			partitionIdx+=1
	array[partitionIdx], array[endIdx] = array[endIdx], array[partitionIdx] 
	return partitionIdx
