def nonConstructibleChange(coins):
	#Time Complexity: O(nlogn), because of the sort() function
	#Space Complexity: O(1), no additional space created
    coins.sort()
	change = 0
	for coin in coins:
		#Most important part. If we ever reach a point where the coin we are checking is greater than change + 1, that means we can never make that value. 
		if coin > change + 1:
			return change + 1
		change += coin
	#If we are able to loop through, we will return the change + 1, and that will be our minimum value. 
	return change + 1

