# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	# O(N) time for buildHeap | O(1) space
    def buildHeap(self, array):
        # Write your code here.
		lastparentIdx = (len(array) - 2)//2 # IMP. -2, we gotta start from the last parent
		for currentIdx in reversed(range(lastparentIdx+1)):
			self.siftDown(currentIdx, len(array)-1, array)
		return array
        
	# O(logN) time for siftDown since this is similar to a binary value search | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
		childOneIdx = currentIdx*2 + 1
		while childOneIdx <= endIdx: # while we have a valid childOneIdx
			childTwoIdx = currentIdx*2 + 2 if currentIdx*2 + 2 <= endIdx else -1
        	if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else: # else if childTwo doesn't exist or childOne is smaller than childTwo
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx*2 + 1
			else: # this means our current node is smaller than both of our child nodes and its in the correct position
				return
				
	# O(logN) time for siftUp since this is similar to a binary value search | O(1) space
    def siftUp(self, currentIdx, heap):
        # Write your code here.
		parentIdx = (currentIdx-1)//2
        while currentIdx>0 and heap[parentIdx]>heap[currentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx-1)//2
	
	# O(1) time | O(1) space
    def peek(self):
        # Write your code here.
		return self.heap[0] # just return the min value of the heap or the root of the tree/first value in the array
        
	# O(logN) time for remove | O(1) space
	def remove(self):
        # Write your code here.
		self.swap(0, len(self.heap)-1, self.heap) # swap the first value (min value) and the last value
		valueToRemove = self.heap.pop() # pop the root node (min value) from the heap
		self.siftDown(0, len(self.heap)-1, self.heap)
		return valueToRemove
        
	# O(logN) time for insert | O(1) space
    def insert(self, value):
        # Write your code here.
		self.heap.append(value)
		self.siftUp(len(self.heap)-1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
