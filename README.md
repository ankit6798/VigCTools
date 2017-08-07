# VigCTools
Vigenere Cipher - Encrypt, Decrypt and Crack

Usage: 

To cipher a text with a key `python vig.py -k somekey -p "some text to cipher"`<br />
To de-cipher a text with a key `python vig.py -k somekey -c "cipher text goes here"`

To crack the key we need a sample clear text and it's ciphered version and to guess the key length...

`python vig.py -c "some cipher text" -p "the clear text" -l key_len_int`

This will output the key in the length requested, if the length is longer than the key then you will see it repeat if not then try a longer key just in case...

TODO: Remove key length and auto calculate the length
