
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

