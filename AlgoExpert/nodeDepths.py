#Iterative Solution
#O(n) time: Only need to traverse through the tree once
#O(h) space: where h is the height of the tree
def nodeDepths(root):
	sumOfDepths = 0
	#Declare a stack to hold the information of both the node being popped, as well as its depth
	stack = [{"node" : root, "depth": 0}]
	#As long as the stack is still populated, the while loop will still be used.
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		#Adding the children nodes to the stack to be added to our sum. 
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
