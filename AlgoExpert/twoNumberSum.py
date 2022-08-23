#Solution using Map
#O(n) time since we are iterating through array a single time
#O(n) space since we are creating a dictionary
def twoNumberSum(array, targetSum):
    nums = {}
	for i in array:
		complement = targetSum - i
		if complement in nums:
			return [complement, i]
		else:
			#Store number in Hash Table
			nums[i] = True
	return []
		
		
    
