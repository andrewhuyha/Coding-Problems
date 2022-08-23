#Solution using 2 pointers
#Tradeoff: Worst time complexity, but better space complexity
#O(nlogn) time
#O(1) space, no extra space created 
def twoNumberSum(array, targetSum):
	#Two pointer technique requires that the input array be sorted
	array.sort()
    left = 0
	right = len(array) - 1
	while left < right:
		currentSum = array[left] + array[right]
		#If the number at the left pointer and the right pointer equals the target, we've found our solution
		if currentSum == targetSum:
			return [array[left], array[right]]
		#If the sum is less than the target, we must move the left pointer over by 1 to get a bigger number
		elif currentSum < targetSum:
			left += 1
		#If the sum is greater than the target, we must move the right pointer backwards by 1 to get a smaller number
		elif currentSum > targetSum:
			right -= 1
	return[]
