class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Time Complexity: O(n), number of nodes in the tree
#Space Complexity: O(d), d is the depth of the tree
def validateBst(tree):
	return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
	#Base Case
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
