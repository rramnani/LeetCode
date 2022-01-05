# Brute force - in-order BST traversal
# O(N) time, O(N) space
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
	result = []
	helper(tree, result)
	print(result)
    return result[-k]

def helper(root, result):
	if root is not None:
		helper(root.left, result)
		result.append(root.value)
		helper(root.right, result)
