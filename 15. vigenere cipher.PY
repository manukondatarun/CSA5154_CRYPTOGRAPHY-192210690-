def vigenere_encrypt(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper()
    encrypted_text = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Encrypt the character
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabet characters are added directly
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    ciphertext = ciphertext.upper()
    decrypted_text = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Decrypt the character
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabet characters are added directly
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Example usage
print("Tarun(192210690)")
key = "KEY"
plaintext = "HELLO WORLD"

encrypted = vigenere_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")

decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
