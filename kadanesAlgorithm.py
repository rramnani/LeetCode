# O(N) time, O(1) space since we are storing just 2 variables
# Dynamic programming
def kadanesAlgorithm(array):
    # Write your code here.
	maxEndingHere = array[0]
	maxSoFar = array[0]
	#print(maxSoFar, array[0], array)
	for num in array[1:]:
		maxEndingHere  = max(num, maxEndingHere+num)
		maxSoFar = max(maxSoFar, maxEndingHere)
		#print(maxSoFar, num, array)
	return maxSoFar
    pass
