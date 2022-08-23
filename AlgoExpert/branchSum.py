#Recursive Implementation
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Time Complexity: O(n) time, we must visit every node in the tree
#Space Complexity: O(n) space, as we must build the solution list. 
def branchSums(root):
	#Final Solution list
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums):
	#Base Case
	if node is None:
		return
	#Calculate for every child's children
	newRunningSum = runningSum + node.value
	#If we've reached a leaf node that has no children, we've reached the bottom of the tree and we can append the newRunningSum to our solution. 
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	
	#Recursively call the function on both sides. 
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)
