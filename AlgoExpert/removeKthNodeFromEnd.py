# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#2 Pointer Pattern
#Time Complexity: O(n) traverse through linked list once
#Space Complexity: O(1), no additional space created
#Goal: Remove the Kth Node from the END
def removeKthNodeFromEnd(head, k):
	#Need to keep track of how far our second pointer has traversed
	counter = 1
	first = head
	second = head
	#Keep the second pointer ahead and traverse til it reaches the kth node
	while counter <= k:
		second = second.next
		counter += 1
	#EDGE CASE: Check to see if the second pointer is already at NULL
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	#If we have not reached NULL, we will continue to increment both pointers
	#first pointer will be pointed at the value BEFORE the kth node
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next
	
		
