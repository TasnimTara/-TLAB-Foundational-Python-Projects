import sys

word = "hello world"
new_word = " "

def encrypt(word, k):
    # for each letter in our message
        #encrypt
    for l in word:
        val = ord(l) + key 
        result = chr(value)
        print(result)
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
