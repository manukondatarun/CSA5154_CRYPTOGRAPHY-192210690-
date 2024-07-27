def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            key_index = i % key_length
            shift = ord(key[key_index].lower()) - ord('a')
            encrypted_char = chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def main():
    print("Tarun(192210690)")
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
