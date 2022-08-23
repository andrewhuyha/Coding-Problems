# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        #Setting the passed in node as the head of the linked list.
        if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

    def setTail(self, node):
        #Setting the passed in node as the tail of the linked list.
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

	#Method for inserting a node before a given node. 
    def insertBefore(self, node, nodeToInsert):
		#Edge case for if the linked list we are inserting to is empty. 
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	#Method for inserting a node after a given node. 
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert
			

    def insertAtPosition(self, position, nodeToInsert):
		#Dealing with the head position
		if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		#Traverse through the linked list until we reach the position we are trying to insert at. 
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition +=1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		#Otherwise, we are dealing witht he tail position. 
		else:
			self.setTail(nodeToInsert)
			

	#Removes all nodes with the given value. Uses both the searching method as well as the remove method. 
    def removeNodesWithValue(self, value):
        node = self.head
		while node is not None:
			#Need to store in a temporary variable so that we can keep track of pointers. 
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
				
	#Removes any node with the value of the node given. 
    def remove(self, node):
		#Also takes care for in case we only have one element in the linked list. 
		#If we are at the head, we will update so that we are at the next node
		if node == self.head:
			self.head = self.head.next
		#If we are at the tail, we 
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

	#Checks to see if the value we are looking for is in the linked list
    def containsNodeWithValue(self, value):
        node = self.head
		#As long as we don't have an empty linked list or we are not at the end of the list we will check to see if we have found the value. 
		while node is not None and node.value != value:
			node = node.next
		#If the the next node is not None that means that it will return false if there is no node for the given value, and return true if it was found. 
		return node is not None
			
	#Helper method to help us remove extra pointers after removal. Order of implementation is very important. 
	def removeNodeBindings(self, node):
		#If we have a node in the previous element. 
		if node.prev is not None: 
		#We reassign where the node is pointing at. 
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None
