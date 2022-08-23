#Non-Optimal Implementaion using an array instead of a Heap
#Time Complexity: O(v^2 + e) | Space Complexity: O(V)
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
	
	#Set the distance of all edges to infinity to start. 
	minDistances = [float("inf") for _ in range(numberOfVertices)]
	#Make sure that we are starting at the first node. 
	minDistances[start] = 0
	
	visited = set()
	
	#As long as we haven't visited all of our vertices, we will stay inside the while loop
	while len(visited) != numberOfVertices:
		vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
		
		#iF we reach a point, where the value is infinity, we know that there is no way to ever reach that vertex
		if currentMinDistance == float('inf'):
			break
		#Add the vertex to the set
		visited.add(vertex)
		
		#Check if the current edge will lead us to a shorter path, or if we can contiune on
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
			if destination in visited:
				continue
				
			newPathDistance = currentMinDistance + distanceToDestination
			currentDestinationDistance = minDistances[destination]
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance
				
	#At the end, if we have any values that still have an infinity value, we will change that value to negative 1
	return list(map(lambda x: -1 if x == float('inf') else x, minDistances))
				
			
		
def getVertexWithMinDistance(distances, visited):
	currentMinDistance = float('inf')
	vertex = None
	
	for vertexIdx, distance in enumerate(distances):
		if vertexIdx in visited:
			continue
		if distance <= currentMinDistance:
			vertex = vertexIdx
			currentMinDistance = distance
			
	return vertex, currentMinDistance
		
