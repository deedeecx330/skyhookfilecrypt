import os, random
from Crypto.Cipher import AES

def encryptFile(originalName, newName, key):
    if not os.path.isfile(originalName):
        raise(FileNotFoundError("Could not find {}!".format(originalName)))
    if len(newName) == 0:
        raise(Exception("Cannot output to a nameless file!"))
    separator = b" :><:><:><: "
    bytesKey = bytes(str(key), 'utf8')
    if len(bytesKey) == 0:
        raise(Exception("Empty passphrase (key)!"))
    elif len(bytesKey) < 32:
        bytesKey = bytesKey + b"\0" * (32 - len(bytesKey))
    else:
        bytesKey = bytesKey[:-(len(bytesKey) - 32)]
    with open(originalName, "rb") as infile:
        iv = os.urandom(16)
        cipher = AES.new(bytesKey, AES.MODE_CBC, iv)
        content = infile.read()
        encryptedContents = cipher.encrypt(content + b"\0" * (AES.block_size - len(content) % AES.block_size))
    with open(newName, "wb") as outfile:
        outfile.write(iv + separator + encryptedContents)

def decryptFile(oldName, newName, key):
    if not os.path.isfile(oldName):
        raise(FileNotFoundError("Could not find {}!".format(oldName)))
    if len(newName) == 0:
        raise(Exception("Cannot output to a nameless file!"))
    separator = b" :><:><:><: "
    bytesKey = bytes(str(key), 'utf8')
    if len(bytesKey) == 0:
        raise(Exception("Empty passphrase (key)!"))
    elif len(bytesKey) < 32:
        bytesKey = bytesKey + b"\0" * (32 - len(bytesKey))
    else:
        bytesKey = bytesKey[:-(len(bytesKey) - 32)]
    with open(oldName, "rb") as infile:
        iv, contents = infile.read().split(separator)
        cipher = AES.new(bytesKey, AES.MODE_CBC, iv)
        decryptedContents = cipher.decrypt(contents).rstrip(b"\0")
    with open(newName, "wb") as outfile:
        outfile.write(decryptedContents)