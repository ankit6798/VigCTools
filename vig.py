#!/usr/bin/env python

from argparse import ArgumentParser

vt = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'],
    ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
    ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C'],
    ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
    ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E'],
    ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'],
    ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
    ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
    ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
    ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
    ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
    ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
    ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
    ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
    ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
    ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
    ['W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
    ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'],
    ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
    ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
]

def enc(o, k):
    r = []
    kl = len(k)
    i = -1
    
    for c in o:
        i += 1
        
        if not is_valid_char(c):
            r.append(c)
            continue
            
        r.append(vt[get_index_from_letter(c)][get_index_from_letter(k[i % kl])])
        
    return ''.join(r)

def dec(s, k):
    r = []
    kl = len(k)
    i = 0
    
    for c in s:
        if not is_valid_char(c):
            r.append(c)
            continue
        
        col = get_index_from_letter(k[i % kl])
        row = 0

        for l in vt:
            if l[col] == c.upper():
                break

            row += 1

        i += 1

        r.append(get_letter_from_index(row))
    
    return ''.join(r)
    
def get_key(o, e, l):
    k = []
    i = -1
    
    for c in o:
        i += 1
        
        if not is_valid_char(c):
            continue
        
        row = get_index_from_letter(c)
        col = vt[row].index(e[i].upper())
        
        k.append(get_letter_from_index(col))
        
    return ''.join(k[:l])
    
def is_valid_char(c):
    return (ord('a') <= ord(c) and ord('z') >= ord(c)) or (ord('A') <= ord(c) and ord('Z') >= ord(c))
    
def get_index_from_letter(l):
    return ord(l.upper()) - ord('A')
    
def get_letter_from_index(i):
    return unichr(i + ord('A'))
       
if __name__ == '__main__':
    parser = ArgumentParser(description='Enc/Dec/Crack Vigenere Ciphers')
    
    parser.add_argument(
        '-c', '--ciphertext', 
        type=str,
        help='The cipher text to work with'
    )
    parser.add_argument(
        '-p', '--cleartext', 
        type=str,
        help='The clear text to work with'
    )
    parser.add_argument(
        '-k', '--key',
        type=str,
        help='The key for the cipher'
    )
    parser.add_argument(
        '-l', '--keylen',
        type=int,
        default=5,
        help='The length of the key [ DEFAULT: 5 ]'
    )
    parser.add_argument(
        '-a', '--action',
        required=True,
        help='(enc, dec, crk) Encrypt: must provide clear text and key. Decrypt: must provide cipher text and key. Crack - Find the key: must provide clear text, cipher text and key length'
    )
    
    args = parser.parse_args()
    
    if args.action == 'enc':
        if args.cleartext is None or args.key is None:
            print "Error: have to supply clear text and key for enc action"
        else:
            print "Encrypted message: %s" % (enc(args.cleartext, args.key))
    elif args.action == 'dec':
        if args.ciphertext is None or args.key is None:
            print "Error: have to supply cipher text and key for dec action"
        else:
            print "Encrypted message: %s" % (dec(args.ciphertext, args.key))
    elif args.action == 'crk':
        if args.cleartext is None or args.ciphertext is None or args.keylen is None:
            print "Error: have to supply clear text and cipher text and key len for crk action"
        else:
            print "Encrypted message: %s" % (get_key(args.cleartext, args.ciphertext, args.keylen))
    else:
        print "Error: -a/--action has to be one of: enc, dec or crk. use -h to see help"
