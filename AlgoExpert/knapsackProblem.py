def knapsackProblem(items, capacity):
	#Time Complexity: O(nc), where n is the number of items, and c is the capacity of our bag.
	#Space Complexty: O(nc), because of the 2-D array we've built.
	
	#We want to build our 2-D array, and fill the first row with 0s, this will be when there are no items in bag. 
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
	#Then, we iterate through and begin populating our array.
	for i in range(1, len(items) + 1):
		currentWeight = items[i -1][1]
		currentValue = items[i - 1][0]
		for c in range(0, capacity + 1):
			if currentWeight > c:
				knapsackValues[i][c] = knapsackValues[i - 1][c]
			else:
				knapsackValues[i][c] = max(knapsackValues[i-1][c], knapsackValues[i - 1][c- currentWeight] + currentValue)
	return [knapsackValues[-1][-1], getKnapSackItems(knapsackValues, items)]

def getKnapSackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i-1][c]:
			i -= 1
		else:
			sequence.append(i-1)
			c -= items[i-1][1]
			i -= 1
		if c == 0:
			break
	return list(reversed(sequence))
	
