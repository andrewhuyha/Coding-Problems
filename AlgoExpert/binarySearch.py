#Iterative Method
#O(logn) time | o(1) space

def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]
		if target == potentialMatch:
			return middle
		elif target < potentialMatch:
			right = middle - 1
		else:
			left = middle + 1
	return -1
	
