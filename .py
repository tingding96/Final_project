alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = "~!@#$%^&*()_-+=`;1234567890{}|[]\:'<>?,./"

key = input("Please choose an encryption key. Key can only contain letters: ")

def has_num(inputString):
	return any(char.isdigit() for char in inputString)

def create_ciphertext_alphabet(key):
	ciphertext_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	for i in range(0,len(key)):
		index = ciphertext_alphabet.index(key[i])
		ciphertext_alphabet.append(key[i])
		ciphertext_alphabet.pop(index)
	return ciphertext_alphabet

def valid_key(key):
	if any((c in symbols) for c in key):
    		print("Not a valid key, please try again. Key can only contain letters.")
	else:
     		print("Valid key: Please enter the phrase you would like to encrypt")
     		
def encrypt(word, ciphertext_alphabet):
	newword = []
	for item in word:
		newword.append(ciphertext_alphabet[alphabet.index(item)])
	return "".join(newword)
	
def encrypt_letter(letter, ciphertext_alphabet):
	return (ciphertext_alphabet[alphabet.index(letter)])
	
def translate(phrase, ciphertext_alphabet):
	newphrase = []
	lowercase = phrase.lower()
	for item in lowercase:
		if item == " ":
			newphrase.append(" ")
		elif item.isalpha():
			newphrase.append(encrypt_letter(item))
	return "".join(newphrase)
	
key = raw_input("Please choose an encryption key. Key can only contain letters: ")
while valid_key(key) == False:
	key = raw_input("Key can only contain letters, try again: ")

print("Your key is " + key)

ciphertext_alphabet = create_ciphertext_alphabet(key)

"""if valid_key(key) == True:
	print ("Valid key")
else:
	print ("Key can only contain letters, try again")"""

phrase = raw_input("What phrase would you like to encrypt?: ")

print(translate(phrase, ciphertext_alphabet))
