from Crypto.Cipher import AES

import sys
import requests
import hashlib
import binascii

'''
Cracking function to perform the following steps to attempt to crack our flag:
    - Prepare the key into a bytearray using our current word from the word list
    - Create the new AES cipher using said key and then attempt decryption
    -  Once we obtain the deciphered result, we need to check that the first part of the resulting bytes object match the cryptohaqck flag standard to find our flag
'''
def crack(x,flag):
    x=x.strip()
    keyHexString = hashlib.md5(x.encode()).hexdigest()
    potentialKey = bytes.fromhex(keyHexString)
    ciphertext = bytes.fromhex(flag)

    aesCipher = AES.new(potentialKey,AES.MODE_ECB)
    plaintext = aesCipher.decrypt(ciphertext)
    plaintext = bytearray.fromhex(plaintext.hex())

    if "crypto{".encode() in plaintext:
        print("We found it: ")
        print(plaintext.decode('utf-8'))
        return plaintext


# Need to obtain the original encrypted flag before beginning the cracking procedure
result = requests.get("https://aes.cryptohack.org/passwords_as_keys/encrypt_flag")
encryptedFlag = result.json()["ciphertext"]
print(encryptedFlag)

# Using list comprehension we can quickly attempt to crack using our supplied words list and print the key once found.
# Voila, we've got it
with open('words','r') as rainbowTable:
    [crack(x,encryptedFlag) for x in rainbowTable]