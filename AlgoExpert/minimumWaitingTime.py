def minimumWaitingTime(queries):
	#Time Complexity: O(nlogn), because of sort() function | Space Complexity: O(1), no additional space created
	
    queries.sort()
	waitingTime = 0
	for i, duration in enumerate(queries):
		queriesLeft = len(queries) - (i + 1)
		waitingTime += duration * queriesLeft
	
    return waitingTime
