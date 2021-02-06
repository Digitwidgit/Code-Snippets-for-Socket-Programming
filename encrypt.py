from cryptography.fernet import Fernet
import os



key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print ("The key was created ")



f = Fernet(key)
#A textfile named secret will have to be created for the example.
with open('secret.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_secret.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
print("The file was encrypted")

os.startfile('mykey.key')




#***************************************
#***************************************

    #Decrypt the same file.

thekey = input("Please enter the decryption key.. > ")
f = Fernet(thekey)

with open('enc_secret.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_secret.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

print("The file has been decrypted")

os.startfile('dec_secret.txt')

