#Time Complexity: O(nlog(n))
#Space Complexity: O(log(n))
def quickSort(array):
	quickSortHelper(array, 0, len(array) - 1)
	return array
	
def quickSortHelper(array, startIndex, endIndex):
	#Base Case
	if startIndex >= endIndex:
		return
	#Declaring the starting points for the pivot, left index, and right index.
	pivotIndex = startIndex
	leftIndex = startIndex + 1
	rightIndex = endIndex
	#Main while loop to stay inbounds as long as our right index is greater than our left index
	while rightIndex >= leftIndex:
		#If number at the left index is greater than the pivot AND the number at the right index is less than the pivot, we will swap the two. 
		if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
			swap(leftIndex, rightIndex, array)
		#If the number at the left index is less than or eqaul to the pivot, we will increment the left index by one. 
		if array[leftIndex] <= array[pivotIndex]:
			leftIndex += 1
		#If the number at the right index is greater than or eqaul to the pivot, we will decrease the right index by one. 
		if array[rightIndex] >= array[pivotIndex]:
			rightIndex -= 1
	#Once we are out of the loop, we will swap the pivot with the number at the right index
	swap(pivotIndex, rightIndex, array)
	#Checking to see if we should apply quick sort to the left subarray first or the right subarray
	leftSubarrayIsSmaller = rightIndex - 1 - startIndex < endIndex - (rightIndex + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIndex, rightIndex -1 )
		quickSortHelper(array, rightIndex + 1, endIndex)
	else:
		quickSortHelper(array, rightIndex + 1, endIndex)
		quickSortHelper(array, startIndex, rightIndex -1 )

#Swapping helper function
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
