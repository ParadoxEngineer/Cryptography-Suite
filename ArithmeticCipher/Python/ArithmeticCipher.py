####################################################################
## Author: Jonathan Edwards
## File name: ArithmeticCipher.py
## Usage: python3 ArithmeticCipher.py {-e | -d} integer-key plain.txt 
## cipher.txt
## Program Purpose: Encrypts and decrypts a text file 
## using a simple arithmetic cipher and a nonnegative integer key
## 
## Program Limitations: None known
##
## Development Computer: Dell Inspiron 15
## Operating System: Windows 10
## Integrated Development Environment (IDE): Notepad++
## Compiler: Python 3.7 well not really because it's not a compiler...
## Build Directions: python3 ArithmeticCipher.py
####################################################################

import sys
import os.path

####################################################################
## Function Name: encrypt()
## Funciton Description: Takes input from standard input character
## by character, adds the key parameter to each and prints to
## standard output.
## Parameter key: The key, an integer, to be added to each character
## in standard input.
## Return: None, all output is through standard output.
####################################################################
def encrypt(key):
	plainText = input()
	
	x = 0
	while(True):
		# Read Character
		text = plainText[x:(x+1)]
		if not text:
			break
		
		# Add Key
		text = int(hex(ord(text)), 16)
		text = (text + key) % 120
		text = chr(text)
		
		# Output text
		print(text, end = "")
		x += 1
	
	sys.stderr.write("Encryption is done")

####################################################################
## Function Name: decrypt()
## Funciton Description: Takes input from standard input character
## by character, subtracts the key parameter to each and prints to
## standard output.
## Parameter key: The key, an integer, to be subtracted from each
## character in standard input.
## Return: None, all output is through standard output.
####################################################################
def decrypt(key):
	cipherText = input()
	
	x = 0
	while(True):
		# Read Character
		text = cipherText[x:(x+1)]
		if not text:
			break
		
		# Add Key
		text = int(hex(ord(text)), 16)
		text = (text - key) % 120
		text = chr(text)
		
		# Output text
		print(text, end = "")
		x += 1
	
	sys.stderr.write("Decryption is done")

def main():
	encrypting = True
	key = 0
	
	if(len(sys.argv) < 3):
		sys.stderr.write("Usage: Edwards1.exe {-e | -d} integer-key <plain-file> <cipher-text>\n")
		return 0
	
	if(sys.argv[1] == "-e"):
		encrypting = True
	elif(sys.argv[1] == "-d"):
		encrypting = False
	else:
		sys.stderr.write("Usage: Edwards1.exe {-e | -d}\n")
		return 0
	
	key = int(sys.argv[2])
	
	if(key <= 0 or key >= 120):
		sys.stderr.write("Usage: Integer key must range between 0 and 120 inclusive\n")
		return 0
	
	if(encrypting):
		encrypt(key)
	else:
		decrypt(key)

if __name__ == "__main__":
	main()