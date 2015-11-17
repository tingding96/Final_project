alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

key = input("Please choose an encryption key. Key can only contain letters: ")
print ("Your key is" + key)

def has_num(inputString):
	return any(char.isdigit() for char in inputString)

def create_ciphertext_alphabet_from(key):
	ciphertext_alphabet = alphabet
	for item in range(0,len(key)):
		key.append(ciphertext_alphabet[i])
		key.pop(key[i])
	return ciphertext_alphabet


def valid_key(key)
	if has_num(key) == True:
		return True
	else: 
		return False
