import os
from Crypto.Cipher import AES

separator = b" :><:><:><: "

def pad(content):
    return(content + b"\x00" * (AES.block_size - len(content) % AES.block_size))

def encryptFile(originalName, newName, key):

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

        toWrite = cipher.encrypt(toCrypt)
        outFile.write(toWrite)

    inFile.close()
    outFile.close()


def decryptFile(oldName, newName, key):

    inFile = open(oldName, "rb")
    iv, content = inFile.read().split(separator)

    length = int(len(content) / AES.block_size)

    skip = len(iv + separator)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    outFile = open(newName, "wb")

    for i in range(0, length):

        inFile.seek(i * AES.block_size + skip)
        content = inFile.read(AES.block_size)

        toWrite = cipher.decrypt(content)

        if i == length - 1:
            toWrite = toWrite.rstrip(b"\x00")

        outFile.write(toWrite)

    inFile.close()
    outFile.close()
