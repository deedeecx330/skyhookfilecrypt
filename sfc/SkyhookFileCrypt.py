import os, random
from Crypto.Cipher import AES

def encryptFile(originalName, newName, key):

    def pad(content):
        return(content + b"\x00" * (AES.block_size - len(content) % AES.block_size))

    separator = b" :><:><:><: "

    iv = os.urandom(16)

    outFile = open(newName, "wb")
    outFile.write(iv + separator)

    inFile = open(originalName, "rb")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    length = int(len(pad(inFile.read())) / AES.block_size)

    for i in range(0, length):
        
        inFile.seek(i * AES.block_size)
        
        if i == length - 1:
            toCrypt = pad(inFile.read(AES.block_size))
        else:
            toCrypt = inFile.read(AES.block_size)
            
        encContent = cipher.encrypt(toCrypt)
        outFile.write(encContent)

    inFile.close()
    outFile.close()

def decryptFile(oldName, newName, key):

    def extractData(filename):
        
        inFile = open(filename, "rb")
        iv, content = inFile.read().split(separator)
        inFile.close()
        
        inFile = open(filename, "wb")
        inFile.seek(0)
        inFile.truncate()
        inFile.write(content.rstrip(b"\x00"))
        inFile.close()
        
        inFile = open(filename, "rb")
        length = int(len(content) / AES.block_size)
        
        return(iv, length, inFile)

    separator = b" :><:><:><: "

    iv, length, inFile = extractData(oldName)
    outFile = open(newName, "wb")

    cipher = AES.new(key, AES.MODE_CBC, iv)

    for i in range(0, length):
        
        inFile.seek(i * AES.block_size)
        content = inFile.read(AES.block_size)
        
        if i == length - 1:
            decContent = cipher.decrypt(content).rstrip(b"\x00")
        else:
            decContent = cipher.decrypt(content)
            
        outFile.write(decContent)

    inFile.close()
    outFile.close()
