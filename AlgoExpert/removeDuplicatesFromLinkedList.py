# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time since we are only iterating through the linkedlist once
#O(1) space since we are doing the modifications in the linked list and thus no extra space needed.
def removeDuplicatesFromLinkedList(linkedList):
	#The pointer for where the current node starts and iterates through
	currentNode = linkedList
	#While loop to check to see if the current node has reached the end of the linked list
	while currentNode is not None:
		#Setting distinct node to the node after current node
		nextDistinctNode = currentNode.next
		#First, make sure that nextDistinctNode is not empty and then check to see if the two values are equal
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			#Everytime the values match, we will move the pointer to next node.
			nextDistinctNode = nextDistinctNode.next
		#Once the next distinct value is found, we will put the pointer there and the excess will be removed
		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode
	#Return the modified list
	return linkedList
			
			
