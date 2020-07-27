# skyhookfilecrypt
File encryption and decryption module extracted from Skyhook: https://github.com/deedeecx330/skyhook

# Usage
To use SFC, simply import it into your Python 3 project:
```
import sfc
```
The module has two functions, encryptFile and decryptFile. Both take 3 arguments: File that is to be encrypted/decrypted, output file where encrypted/decrypted contents will be saved to and a passphrase to encrypt/decrypt the file with.

Simply calling the functions like so:
```
sfc.encryptFile('test.txt', 'test.sky', 3.14)
```
will encrypt <i>test.txt</i> and save it as a new file called <i>test.sky</i>. The process can be reversed by using:
```
sfc.decryptFile('test.sky', 'test.txt', 3.14)
```
