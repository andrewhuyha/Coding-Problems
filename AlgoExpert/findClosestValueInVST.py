#Recursive Implementation
#Time Complexity: O(log(n)) time, because we are cutting the tree in half everytime we explore a node.
#Space Complexity: O(log(n))
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)
    
def findClosestValueInBstHelper(tree, target, closest):
	#Base Case: When we reach the bottom of leaf
	if tree is None:
		return closest
	#If absolute difference between the target and closest is larger than the value we have in the absolute 
	#difference between target and the tree, we will update closest value to the tree value.
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	#If the target is less the value in the tree, we will call the helper method on the left subtree. 
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	#If the target is greater the value in the tree, we will call the helper method on the right subtree. 
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	#If we find a value equal to the target
	else:
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
