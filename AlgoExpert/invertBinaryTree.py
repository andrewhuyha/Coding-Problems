#Iterative Solution
#Time Complexity: O(n), only to traverse through the tree once
#Space Complexity: O(n), need to create queue which will at some point hold all the leaf nodes
def invertBinaryTree(tree):
	#Initilize queue to store the value of the tree
    queue = [tree]
	#Continue to work through as long as the queue is populated
	while len(queue):
		current = queue.pop(0)
		#If we run into a null value, we will continue
		if current is None:
			continue
		#Swap
		swapLeftAndRight(current)
		queue.append(current.left)
		queue.append(current.right)

#Swap Helper Function
def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
