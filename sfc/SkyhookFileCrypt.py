import os, threading
from Crypto.Cipher import AES

separator = b" :><:><:><: "

lock = threading.Lock()

def enCrypt(aesCipher, outHandle, content, tthread):

    encContent = aesCipher.encrypt(content)

    if tthread == None:
        with lock:
            outHandle.write(encContent)
            return(0)

    while tthread.is_alive == True:
        pass

    with lock:
        outHandle.write(encContent)
        return(0)

def pad(content):
    return(content + b"\x00" * (AES.block_size - len(content) % AES.block_size))

def encryptFile(originalName, newName, key):

    iv = os.urandom(16)

    outFile = open(newName, "wb")
    outFile.write(iv + separator)

    inFile = open(originalName, "rb")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    length = int(len(pad(inFile.read())) / AES.block_size)

    previous = None
    threads = list()

    for i in range(0, length):

        inFile.seek(i * AES.block_size)

        if i == length - 1:
            toCrypt = pad(inFile.read(AES.block_size))
        else:
            toCrypt = inFile.read(AES.block_size)

        thread = threading.Thread(target=enCrypt, args=(cipher, outFile, toCrypt, previous,))
        threads.append(thread)
        previous = thread

    for thread in threads:
        thread.start()
        thread.join()

    inFile.close()
    outFile.close()

def deCrypt(aesCipher, outHandle, content, tthread, padded):

    decContent = aesCipher.decrypt(content)

    if tthread == None:
        with lock:
            outHandle.write(decContent)
            return(0)

    while tthread.is_alive == True:
        pass

    with lock:

        if padded == True:
            decContent.rstrip(b"\x00")

        outHandle.write(decContent)
        return(0)

def decryptFile(oldName, newName, key):

    inFile = open(oldName, "rb")
    iv, content = inFile.read().split(separator)

    length = int(len(content) / AES.block_size)

    skip = len(iv + separator)

    outFile = open(newName, "wb")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    previous = None
    threads = list()
    unPad = False

    for i in range(0, length):

        inFile.seek(i * AES.block_size + skip)
        content = inFile.read(AES.block_size)

        if i == length - 1:
            unPad = True

        thread = threading.Thread(target=deCrypt, args=(cipher, outFile, content, previous, unPad,))
        threads.append(thread)
        previous = thread

    for thread in threads:
        thread.start()
        thread.join()

    inFile.close()
    outFile.close()
