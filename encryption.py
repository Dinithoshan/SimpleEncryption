#imports
import random
import string

#create a variable for the avaliable strings
chars = " " + string.punctuation + string.digits + string.ascii_letters
#create a list for the characters
chars = list(chars)
#creating the key
key = chars.copy()

random.shuffle(key)

#uncomment following two lines to check the list
#print (f"chars:{chars}")
#print (f"key:{key}")

#encryption part of the program

ogmsg = input("Enter text to be encrypted: ")
cipher = ""

for letter in ogmsg:
    index = chars.index(letter)
    cipher += key[index]

print (f"original message: {ogmsg}")
print (f"encrypted message: {cipher}")

cipher = input("Enter Cipher to be decrypted: ")
ogmsg = ""

for letter in cipher:
    index = key.index(letter)
    ogmsg += chars[index]

print (f"original message: {cipher}")
print (f"encrypted message: {ogmsg}")