from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()
from setuptools import setup, find_packages

setup(name='skyhookfilecrypt',
    version='1.4',
    packages = find_packages(),
    description='Multithreaded file encryption and decryption module extracted from Skyhook',
    long_description=README,
    long_description_content_type='text/markdown',
    author='deedeecx330',
    url='https://github.com/deedeecx330/skyhookfilecrypt',
    license='GNU General Public Licence v3 (GPLv3)',
    install_requires=['pycryptodome'],
    keywords = "aes cbc encrypt decrypt cryptography file",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities',
    ],
)
