# O(N*logN) time, O(1) space 
def heapSort(array):
	buildMaxHeap(array)
	for endIdx in reversed(range(1, len(array))): # if we're left 1 element, then we're done!
		swap(0, endIdx, array)
		siftDown(0, endIdx -1, array)
    return array

def buildMaxHeap(array):
	firstParentIdx = (len(array) - 1) // 2
	for currentIdx in reversed(range(firstParentIdx + 1)):
		siftDown(currentIdx, len(array) -1, array)
		print(currentIdx, array)

def siftDown(currentIdx, endIdx, heap):
	childOneIdx = currentIdx * 2 + 1
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(idxToSwap, currentIdx, heap)
			currentIdx = idxToSwap
			childOneIdx = currentIdx * 2 + 1
		else: # we're done, the element at currentIdx is in its correct place in the heap
			return 
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
