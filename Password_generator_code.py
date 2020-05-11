import string
import random

if __name__ == "__main__":
	
	s1 = string.ascii_lowercase
	s2 = string.ascii_uppercase
	s3 = string.digits
	s4 = string.punctuations
	
	plen = input("Enter the password length : ")
	
	store = []
	store += s1
	store += s2
	store += s3
	store += s4
	
	random.shuffle(store)
	print(''.join(store[ : plen]))
