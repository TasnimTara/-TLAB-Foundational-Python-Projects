import sys 

first_numeral = ord("A") 
last_numeral = ord("Z")


def encrypt(word, k):
 # Loop through each character in the word
    for char in word:
        # Check if the character is an alphabet letter
            if char.isalpha():
            # Shift the character by 'key' positions
            shift = ord(char) + key
            # If the shifted character goes beyond the alphabet (for lowercase letters)
            if char.islower() and shift > ord('z'):
                shift -= 26
            # If the shifted character goes beyond the alphabet (for uppercase letters)
            elif char.isupper() and shift > ord('Z'):
                shift -= 26
            # Convert the shifted character back to a string and add it to the result
            result += chr(shift)
        else:
            # If the character is not an alphabet letter, add it to the result without changing
            result += char
    # Return the encrypted word
    return result
    
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
