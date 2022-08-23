def caesarCipherEncryptor(string, key):
    #Using only lowercase letters and a non-negative integer key. 
	#In Python, the "ord" fucntion returns the Unicode of a given character. 
	newLetters = []
	newKey = key % 26
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey, alphabet))
	return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
	newLetterCode = alphabet.index(letter) + key
	return alphabet[newLetterCode % 26]
	
