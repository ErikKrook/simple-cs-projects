from cipher import encrypt_ceasar_cipher, decrypt_ceasar_cipher

def test_basic_encrypt_decrypt():
    original = "hej"
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 3)
    assert decrypted == original

def test_empty_string():
    original = ""
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 3)
    assert decrypted == original

def test_known_values():
    assert encrypt_ceasar_cipher("abc", 3) == "def"
    assert decrypt_ceasar_cipher("def", 3) == "abc"

def test_wrong_encrypt():
    original = "hej"
    encrypted = encrypt_ceasar_cipher(original, 3)
    decrypted = decrypt_ceasar_cipher(encrypted, 4)
    assert encrypted != decrypted
