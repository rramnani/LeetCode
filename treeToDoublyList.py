# O(N) time | O(1) space    
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        dummy = Node(-1)
        self.prev = dummy
        self.treeToDoublyListHelper(root)
        head = dummy.right
        
        head.left = None
        dummy.right = None
        # circular
        head.left = self.prev
        self.prev.right = head
        return head
    def treeToDoublyListHelper(self, root):
        if not root:
            return None
        
        self.treeToDoublyListHelper(root.left)
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.treeToDoublyListHelper(root.right)
        
