import string

decrypted_text = ''
encrypted_text = ''
uppercase_alphabet = string.ascii_uppercase
lowercase_alphabet = string.ascii_lowercase
punctuation = string.punctuation
whitespaces = string.whitespace
digits = string.digits

print("ENCRYPTION CYPHER - DO NOT USE DIACRITICS")

text = input("Your text here: ")
key = int(input("Encryption key: "))

def lowercase_encrypt(char):
    encrypted_char_index = (lowercase_alphabet.index(char) + key) % 26
    encrypted_text = encrypted_text + lowercase_alphabet[encrypted_char_index]
    return (encrypted_text)

def uppercase_encrypt(char):
    encrypted_char_index = (uppercase_alphabet.index(char) + key) % 26
    encrypted_text = encrypted_text + uppercase_alphabet[encrypted_char_index]
    return (encrypted_text)

def encrypt_digit(char):
    encrypted_char_index = (digits.index(char) + key) % 10
    encrypted_text = encrypted_text + digits[encrypted_char_index]
    return (encrypted_text)

#ENCRYPTION
for char in text:

    if char.islower():
        lowercase_encrypt(char)
    elif char.isupper():
        uppercase_encrypt(char)
    elif char.isspace():
        encrypted_text = encrypted_text + char
    elif char.isdigit():
        encrypt_digit()
    else:
        encrypted_text = encrypted_text + char

print (encrypted_text)