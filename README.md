# skyhookfilecrypt
File encryption and decryption module extracted from Skyhook: https://github.com/deedeecx330/skyhook .

# Usage
To use skyhookfilecrypt, simply import it into your Python 3 project.

The module has two functions, encryptFile and decryptFile. The function arguments in both cases are: 
-   File that is to be encrypted/decrypted
-   Output file where encrypted/decrypted contents will be saved to
-   A passphrase to encrypt/decrypt the file with

For example:
```
import skyhookfilecrypt

skyhookfilecrypt.encryptFile(file.in, file.out, password)
```
will encrypt file.in with the given password and write the encrypted contents of file.in to file.out. Same principle works for decrypting files.
