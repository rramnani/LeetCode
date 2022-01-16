# O(N) time, O(N) space
def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)

def constructMinHeightBst(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	midIdx = (startIdx + endIdx) // 2
	newBstNode = BST(array[midIdx])
	print(array[startIdx:endIdx + 1])
	if bst is None: # root node
		bst = newBstNode
	else:
		if array[midIdx] < bst.value: # left subtree
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode # right subtree
			bst = bst.right
	constructMinHeightBst(array, bst, startIdx, midIdx - 1) # left subtree
	constructMinHeightBst(array, bst, midIdx + 1, endIdx) # right subtree
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
