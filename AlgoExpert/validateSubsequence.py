#Time Complexity: O(n), only need to traverse through the main array once.
#Space Complexity: O(1)
#Solution using a while loop
def isValidSubsequence(array, sequence):
	#Declare the two pointers which will iterate through the two arrays, array and sequence. 
	arrayIndex = 0
	sequenceIndex = 0
	#Stays running as long as we have more values to check for
	while(arrayIndex < len(array) and sequenceIndex < len(sequence)):
		#If we have found a match, we will move the pointer forward for the sequence array.
		if array[arrayIndex] == sequence[sequenceIndex]:
			sequenceIndex +=1
		#No matter what, we will continue to move along in the array 
		arrayIndex +=1
	#If the sequence index is equal to the length of the sequence, that means that we have 
	#reached the end of the sequence and that a subsequence has been found.
	return sequenceIndex == len(sequence)
