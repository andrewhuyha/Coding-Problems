#Recursive Solution
#Time Complexity: O(n)
#Space Complexity: O(d), where d is the depth of the tree
def invertBinaryTree(tree):
	#Base Case
	if tree is None:
		return
	swapLeftAndRight(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

#Swap Helper Function
def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
