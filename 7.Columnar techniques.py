def columnar_transposition_encrypt(text, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    matrix = ['' * num_cols for _ in range(num_rows)]
    
    # Fill the matrix with the text
    for i in range(len(text)):
        row = i // num_cols
        col = i % num_cols
        matrix[row] += text[i]
    
    # Read the matrix columns based on the key
    sorted_key = sorted((char, i) for i, char in enumerate(key))
    encrypted_text = ''.join(''.join(matrix[row][sorted_key[i][1]] for i in range(num_cols)) for row in range(num_rows))
    
    return encrypted_text

def columnar_transposition_decrypt(ciphertext, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    num_empty_cells = num_cols * num_rows - len(ciphertext)
    
    # Rebuild the matrix
    sorted_key = sorted((char, i) for i, char in enumerate(key))
    col_order = [i for _, i in sorted_key]
    
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    idx = 0
    for col in col_order:
        for row in range(num_rows):
            if not (row == num_rows - 1 and col >= num_cols - num_empty_cells):
                matrix[row][col] = ciphertext[idx]
                idx += 1

    # Read the matrix rows to get the plaintext
    decrypted_text = ''.join(''.join(matrix[row]) for row in range(num_rows))
    
    return decrypted_text.strip()

# Example usage
print("Tarun(192210690)")
plain_text = "HELLOFROMPYTHON"
key = "KEY"

encrypted = columnar_transposition_encrypt(plain_text, key)
print(f"Encrypted: {encrypted}")

decrypted = columnar_transposition_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
