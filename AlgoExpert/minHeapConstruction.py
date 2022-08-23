
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

	#O(n) time | O(1) Space
    def buildHeap(self, array):
		firstParentIdx = (len(array) - 1 ) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array

	#O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		#As long as there more childs to be explored in the heap
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <=endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

	#O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
		#Forumula for finding index of any child's parent node. // means floor in Python
		parentIdx = (currentIdx - 1)// 2
		#So as long as we are not at the parnet node, and there are values to be swaped, we will call the siftUp function. 
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
		
    def peek(self):
		#Returns the heap's minimum value
		return self.heap[0]

    def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap)- 1, self.heap)
		return valueToRemove

    def insert(self, value):
		#First, insert the value into the heap at the end
		self.heap.append(value)
		#Sift the value upwards if needed. 
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
