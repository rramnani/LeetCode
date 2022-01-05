# Reverse in-order BST traversal
# O(h + k) time, h -> height of the BST, O(h) space for the recursive call stack
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited
		self.latestVisitedNodeValue = latestVisitedNodeValue
		
def findKthLargestValueInBst(tree, k):
	treeInfo = TreeInfo(0, -1)
	reverseInOrderTraverse(tree, k, treeInfo)
	print(treeInfo.numberOfNodesVisited)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
	if node is None or treeInfo.numberOfNodesVisited == k:
		return
	
	reverseInOrderTraverse(node.right, k, treeInfo)
	if treeInfo.numberOfNodesVisited < k:
		treeInfo.numberOfNodesVisited += 1
		treeInfo.latestVisitedNodeValue = node.value
		reverseInOrderTraverse(node.left, k, treeInfo) # call the left node only if numberOfNodesVisited < k
