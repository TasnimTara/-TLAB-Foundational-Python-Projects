import sys 

first_numeral = ord("A") 
last_numeral = ord("Z")

cesear_code = last_numeral - first_numeral + 1



def encrypt(word, k):
    result = ""
    # for each letter in our message
        #encrypt
    for l in first_numeral:
        value = ord(l) + key 
        #the ord function returns the unicode of a character
        result = chr(value)
        print(cesear_code)
        print(result)
return 

def encrypt(word, k):
    result = ""
    # for each result in our message 

    for l in word:
        print("ASCII value before", ord(1))
        value = ord(1) + k
        print("ASCII value", value)
    return


def decrypt(word, k):
    return


if __name__ == "__main__":
    # take in first arg as word
    word = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(word, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)

    print("Your decrypted word is", decrypted)
