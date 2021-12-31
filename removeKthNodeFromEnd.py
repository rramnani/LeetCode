def removeKthNodeFromEnd(head, k):
    # Write your code here.
	#length = len(head)
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
    	counter+=1
	if second is None: # second is pointing to None => First is at the head of linked list
		head.value = head.next.value
		head.next = head.next.next
		return # then we're done here
	while second.next is not None:
		second = second.next
		first = first.next
	
	first.next = first.next.next
    return head
