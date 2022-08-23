class MinMaxStack:
	
	def __init__(self):
		self.minMaxStack = []
		self.stack = []
	
	#Time Complexity O(1) | Space Complexity O(1)
    def peek(self):
		return self.stack[len(self.stack) - 1]

	#Time Complexity O(1) | Space Complexity O(1)
    def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()
	
	#Time Complexity O(1) | Space Complexity O(1)
    def push(self, number):
		newMinMax = {"min": number, "max": number}
		#As long as our stack is not empty...
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
			newMinMax["min"] = min(lastMinMax["min"], number)
			newMinMax["max"] = max(lastMinMax["max"], number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

	#Time Complexity O(1) | Space Complexity O(1)	
    def getMin(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
	
	#Time Complexity O(1) | Space Complexity O(1)		
    def getMax(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
