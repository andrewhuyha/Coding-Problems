def firstNonRepeatingCharacter(string):
	#Time Complexity: O(n), just need to traverse through string once
	#Space Complexity: O(1). because we KNOW that there can be 26 characters at most
	
	#Declare hash table to store letters that we've seen. Can be at most 26 characters.
	characterSeen = {}
	for character in string:
		#If we haven't seen the character before, this will set it's value. Otherwise, it will add 1 to its frequency. 
		characterSeen[character] = characterSeen.get(character, 0) + 1
	
	#Loop through the string, if we see a value that already has a value of 1, that will be the first non-repeating character.
	for i in range(len(string)):
		character = string[i]
		if characterSeen[character] == 1:
			return i
	
    return -1
