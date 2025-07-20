from cipher import encrypt_ceasar_cipher, decrypt_ceasar_cipher, encrypt_vigenere, decrypt_vigenere

def test_ceasar_encrypt_decrypt():
    original = "hej"
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 3)
    assert decrypted == original

def test_ceasar_empty_string():
    original = ""
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 3)
    assert decrypted == original

def test_ceasar_known_values():
    assert encrypt_ceasar_cipher("abc", 3) == "def"
    assert decrypt_ceasar_cipher("def", 3) == "abc"

def test_ceasar_wrong_encrypt():
    original = "hej"
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 4)
    assert encrypted != decrypted

def test_vigenere_encrypt_decrypt():
    original = "hej"
    key = 'liverpool'
    encrypted = encrypt_vigenere(original, key)
    decrypted = decrypt_vigenere(encrypted, key)
    assert decrypted == original

def test_vigenere_empty_string():
    original = ""
    key = 'liverpool'
    encrypted = encrypt_vigenere(original, key)
    decrypted = decrypt_vigenere(encrypted, key)
    assert decrypted == original


def test_cvigenere_wrong_encrypt():
    original = "hej"
    key = 'liverpool'
    encrypted = encrypt_vigenere(original, key)
    decrypted = decrypt_vigenere(encrypted, 'aik')
    assert encrypted != decrypted
