# O(N^2) time, O(N) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
	sequences = [None for x in array]
	sums = array[:] # sum will be at least the value of the element at each index
	maxSumIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum 
				sequences [i] = j
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx] # going to the previous index
	return list(reversed(sequence)) # reverse the list
