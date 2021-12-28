# O( max(n, m) + 1 )  = O(max(n, m))time, the longest linked list will determine the no. of iterations, 1 iteration for the carry
# O( max(n, m) + 1 ) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
		
def sumOfLinkedLists(linkedListOne, linkedListTwo):
	newLinkedListHeadPointer = LinkedList(0)
	currentNode = newLinkedListHeadPointer
	carry = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	print("linkedListOne.value","\t", "linkedListTwo.value", "\t", "value", "\t", "carry")
	# if we're left with no nodes from both the Linked Lists, but we still have a carry
	# then we need to create a new node with that carry as the value value so check for carry!=0
	while nodeOne is not None or nodeTwo is not None or carry != 0:
		# we want check whether we have exhausted either of the linked lists
		valueOne = nodeOne.value if nodeOne is not None else 0 
		valueTwo = nodeTwo.value if nodeTwo is not None else 0 
		sumOfValues = valueOne + valueTwo + carry
		
		newValue = sumOfValues % 10 
		newNode = LinkedList(newValue)
		
		#print(nodeOne.value, "\t" ,nodeTwo.value, "\t" ,newValue, "\t", carry)
		currentNode.next = newNode
		currentNode = newNode
		
		carry = sumOfValues // 10
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
	return newLinkedListHeadPointer.next
