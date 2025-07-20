
def encrypt_ceasar_cipher(text):
    encrypted = ""
    for c in text:
        ceasar_chr = chr(ord(c) + 3)
        encrypted += ceasar_chr
    
    return encrypted

def decrypt_ceasar_cipher(text):
    decrypted = ""
    for c in text:
        ceasar_chr = chr(ord(c) -3)
        decrypted += ceasar_chr
    
    return decrypted

encrypted = encrypt_ceasar_cipher('hej')

print(encrypted)

decrypted = decrypt_ceasar_cipher(encrypted)

print(decrypted)