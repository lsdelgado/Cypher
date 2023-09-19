import string

decrypted_text = ''
encrypted_text = ''
uppercase_alphabet = string.ascii_uppercase
lowercase_alphabet = string.ascii_lowercase
digits = string.digits

print("ENCRYPTION CYPHER - DO NOT USE DIACRITICS")

text = input("Your text here: ")
key = int(input("Encryption key: "))

def lowercase_encrypt(char):
    encrypted_char_index = (lowercase_alphabet.index(char) + key) % 26
    return(lowercase_alphabet[encrypted_char_index])
def uppercase_encrypt(char):
    encrypted_char_index = (uppercase_alphabet.index(char) + key) % 26
    return(uppercase_alphabet[encrypted_char_index])
def digit_encrypt(char):
    encrypted_char_index = (digits.index(char) + key) % 10
    return(digits[encrypted_char_index])

#ENCRYPTION
for char in text:

    if char.islower():
        encrypted_text += lowercase_encrypt(char)
    elif char.isupper():
        encrypted_text += uppercase_encrypt(char)
    elif char.isspace():
        encrypted_text = encrypted_text + char
    elif char.isdigit():
        encrypted_text += digit_encrypt()
    else:
        encrypted_text = encrypted_text + char


print (encrypted_text)