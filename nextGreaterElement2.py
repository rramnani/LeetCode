# Naive: O(N^2) time, O(N) space
def nextGreaterElement(array):
    # Write your code here.
    res = [-1] * len(array)

	for i in range(len(array)):
        for j in range(len(array)):
        	if array[(i + j) % len(array)] > array[i]:
            	res[i] = array[(i + j) % len(array)]
				print("Array o/p ", res)
                break
    return res
