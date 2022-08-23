#O(n) time, need to traverse through the array once.
#O(1) space, no additional space needed. 
def findThreeLargestNumbers(array):
	#Intialize Solution Array starting with null values in all 3 slots
    threeLargest = [None, None, None]
	#Loop through the given array, and put it through our algorithm
	for num in array:
		updateLargest(threeLargest, num)
	return threeLargest

#Function to check comparisons and then shift values to their correct indexes
def updateLargest(threeLargest, num):
	#If the 3rd slot is empty, or the current number we are checking is greater than it, we will insert it, and shift the other numbers backwards.
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate(threeLargest, num, 2)
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)
		
def shiftAndUpdate(array, num, index):
	for i in range(index + 1):
		if i == index:
			array[i] = num
		else:
			array[i] = array[i + 1]
