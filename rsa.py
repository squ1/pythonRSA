import math
import os
import primeGenerator
import random

def generateKeys():
    #Generating N and phi of N
    counter = 1
    primeNumbers = primeGenerator.primeNumberGenerator(100)
    p = random.choice(primeNumbers)
    q = random.choice(primeNumbers)
    N = p * q
    phiN = (p - 1) * (q - 1)

    #Generating e (public)
    for i in range(2, phiN - 1):
        if math.gcd(i, phiN) == 1:
            e = i
            break

    #Generating d (private)
    while True:
        number = e * counter
        if (number * e) % phiN == 1:
            d = number
            break
        counter += 1

    #Write keys to file
    #Private key
    private = open("private-key.txt", "w")
    private.write(str(N) + "\n")
    private.write(str(d) + "\n")
    private.close()
    #Public key
    public = open("public-key.txt", "w")
    public.write(str(N) + "\n")
    public.write(str(e) + "\n")
    public.close()

#Encrypt message
def encrypt(publicKeyPath):
    #Getting Key and put it in the variables N and e
    key = open(publicKeyPath, "r")
    keys = key.readlines()
    N, e = keys
    #Cipher
    c = ""
    #Getting message and split into letters
    m = input("Enter your message: ")
    m = list(m)

    #Encrypting message
    for letter in m:
        s = ord(letter)
        s = s**int(e)
        s = s%int(N)
        c += str(s) + "/"

    #Return cipher
    return c

def decrypt(privateKeyPath):
    #Getting keys for decryption
    key = open(privateKeyPath, "r")
    keys = key.readlines()
    N, d = keys
    #Message
    m = ""
    #Getting decrypted message
    c = input("Enter your cipher: ")

    #Decrypting message
    num = c.split("/")
    del num[-1]
    for i in num:
        i = int(i)
        s = i**int(d)
        s = s%int(N)
        s = chr(s)
        m += s

    #Return message
    return m

#Opening keys
publicKeyPath = "./public-key.txt"
privateKeyPath = "./private-key.txt"

#Asking user if keys should be generated
createKeys = input("Do you want to generate keys? (y/n): ")
if createKeys == "y" or createKeys == "Y":
    generateKeys()
elif createKeys == "n" or createKeys == "N":
    if os.path.isfile("public-key.txt") == False:
        publicKeyPath = input("Please enter path to your public key: ")
    if os.path.isfile("private-key.txt") == False:
        privateKeyPath = input("Please enter path to your private key: ")
else:
    print("That's not an option!")

#Asking user if he wants to decrypt or encrypt
deoren = input("Do you want to encrypt or decrypt? (e/d): ")
if deoren == "e" or deoren == "E":
    msgenc = encrypt(publicKeyPath)
    print("Your encrypted message:", msgenc)
elif deoren == "d" or deoren == "D":
    msgdec = decrypt(privateKeyPath)
    print("Your decrypted message:", msgdec)
else:
    print("That's not an option!")