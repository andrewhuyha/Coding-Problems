#Time Complexity: O(nlogn)
#Space Complexity: O(1)

def heapSort(array):
	#Create the Max Heap
    buildMaxHeap(array)
	#Continually, swap the greatest value in the heap with the 
	for endIdx in reversed(range(1, len(array))):
		#The greatest element is at index 0, and you swap it with the number at the end index
		swap(0, endIdx, array)
		#Heapify the element at 0, and put it at the end of the array
		siftDown(0, endIdx - 1, array)
	return array

def buildMaxHeap(array):
		firstParentIdx = (len(array) - 2 ) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
	childOneIdx = currentIdx * 2 + 1
	#As long as there more childs to be explored in the heap
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <=endIdx else -1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(currentIdx, idxToSwap, heap)
			currentIdx = idxToSwap
			childOneIdx = currentIdx * 2 + 1
		else:
			return
		
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
