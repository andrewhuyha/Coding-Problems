# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		#Create Queue 
        queue = [self]
		#While loop for when there are still elements in the queue
		while len(queue) > 0: 
			#The first element of the queue will be popped(FIFO)
			current = queue.pop(0)
			#Add the element to the solution
			array.append(current.name)
			#Add all of the children of the current node to the queue in order
			for child in current.children:
				queue.append(child)
		return array
