#Time Complexity: O(n), only need to traverse through array once | Space Complexity: O(1), no additional space needed
def kadanesAlgorithm(array):
	#Set both maxes to be equal to the first value in the array
	maxEndingHere = array[0]
	maxSoFar = array[0]
	#Iterate through array from the first index til the end.
	for i in array[1:]:
		maxEndingHere = max(i, maxEndingHere + i)
		maxSoFar = max(maxSoFar, maxEndingHere)
	return maxSoFar
