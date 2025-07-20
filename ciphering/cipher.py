
def encrypt_ceasar_cipher(text, shift):
    encrypted = ""
    for c in text:
        ceasar_chr = chr(ord(c) + shift)
        encrypted += ceasar_chr
    
    return encrypted

def decrypt_ceasar_cipher(text, shift):
    decrypted = ""
    for c in text:
        ceasar_chr = chr(ord(c) - shift)
        decrypted += ceasar_chr
    
    return decrypted

def encrypt_vigenere(text, key):
    encrypted = ""
    key_length = len(key)

    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]  # loop over the key
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)  # Use %256 for full byte range
        encrypted += encrypted_char

    return encrypted

def decrypt_vigenere(text, key):
    decrypted = ""
    key_length = len(key)

    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted += decrypted_char

    return decrypted

key = 'lumpa'

encoded = encrypt_vigenere('hej', key)

print(encoded)

print(decrypt_vigenere(encoded, key))
