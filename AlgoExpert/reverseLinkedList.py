# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    p1, p2 = None, head
	while p2 is not None:
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
	return p1

#Solution with more proper variable names
	#prev, current = None, head
	#while current is not None:
		#next = current.next
		#current.next = prev
		#prev = current
		#current = next
	#return prev
