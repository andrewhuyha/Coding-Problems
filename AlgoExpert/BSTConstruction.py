#Iterative Implementation
	#Average Time Complexity: O(log(n))
	#Average Space Complexity: O(1)

	#Worst Time Complexity: O(n)
	#Worst Space Complexity: O(1)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		#Keep track of where we are in the search
		currentNode = self
		while True:
			#Check for if we should explore the left subtree
			if value < currentNode.value:
				#As long as the there is a node to left that doesn't have a child, we are able to insert our value.
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				#If there is already a value there, we will move on to the left tree and keep exploring
				else:
					currentNode = currentNode.left
				#Insertion for right subtree
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self

    def contains(self, value):
        currentNode = self
		#While loop to check if we have more values to compare
		while currentNode is not None:
			#If the value is less than the currentNode we are at, we will explore its left subtree.
			if value < currentNode.value:
				currentNode = currentNode.left
			#If the value is greater than the currentNode we are at, we will explore its right subtree.
			elif value > currentNode.value:
				currentNode = currentNode.right
			#Otherwise, they are equal and we can return true.
			else:
				return True
		#If we never find the value, we return false.
		return False
			
	#More difficult than insertion and searching, as there are many edge cases to consider.
	#3 Possible Edge cases to consider
		#1. Node to be deleted is a leaf: Simply just delete from the tree.
		#2. Node to be deleted only has one child: Copy the child to the node and delete the child
		#3. Node to be deleted has two children: Find inorder successor.
    def remove(self, value, parentNode = None):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode  = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						pass
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
        return self
	
	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value
