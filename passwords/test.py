from passlib.hash import pbkdf2_sha256
import os
import getpass

#Get a hash of the password that is inputted

password = getpass.getpass("Enter that shit:")

hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)

#open the file to write
file = open('test.txt', 'w')
#write the hash to the file
file.write(hash)
#open the file we just wrote to
file = open('test.txt', 'r')
#store the hash value to a string
pls =  file.readline()
#verify the hash and see if it matches the password
print pbkdf2_sha256.verify(password,  pls)
