# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, isBalanced, height):
		self.isBalanced = isBalanced
		self.height = height

def heightBalancedBinaryTree(tree):
  treeInfo = getTreeInfo(tree)
  return treeInfo.isBalanced

# O(N) time, N => no. of nodes, O(h) space, h => height of the binary tree 
def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(True, -1)
	
	leftSubTreeInfo = getTreeInfo(tree.left)
	rightSubTreeInfo = getTreeInfo(tree.right)
	
	isBalanced = (leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1)
	height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
	return TreeInfo(isBalanced, height)
