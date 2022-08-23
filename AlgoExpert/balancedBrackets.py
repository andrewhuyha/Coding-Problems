def balancedBrackets(string):
    #Time Complexity: O(n)), need to traverse through the array once
	#Space Complexity: O(n), checks are in place. 
	
	openingBrackets = "([{"
	closingBrackets = ")]}"
	#Initialize a dictionary that will map each opening bracket to its corresponding closing bracket.
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
	stack = []
	#For loop to iterate through given string
	for char in string: 
		#If we find an open bracket, we will add it to our stack 
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			#If our stack is empty, this means that the openingBracket was not found and that the string is unbalanced. 
			if len(stack) == 0:
				return False
			#If the most recent value in our stack is equal to it's key, we will pop the openingBracket out of our stack.
			if stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	#If at the end of running through the for loop, if the stack is empty, we will know if everything is matched up, thus we can return true, otherwise return False. 
	if len(stack) == 0:
		return True
	return False
