#Time Complexity: O(n^2)
#Space Complexity: O(1)
def insertionSort(array):
	for i in range(1, len(array)):
		j = i
		#While j is not at the beginning and checking to see it is less than the number that comes before.
		while j > 0 and array[j] < array[j -1]:
			#Swap
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array
	
