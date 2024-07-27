import numpy as np

SIZE = 5

def create_table(keyword):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    flag = {ch: False for ch in alphabet}
    table = np.full((SIZE, SIZE), '', dtype=str)
    
    k = 0
    for char in keyword:
        c = char.lower()
        if c == 'j':
            c = 'i'
        if not flag[c]:
            table[k // SIZE][k % SIZE] = c
            flag[c] = True
            k += 1
            
    for char in alphabet:
        if not flag[char]:
            table[k // SIZE][k % SIZE] = char
            flag[char] = True
            k += 1
    
    return table

def playfair_cipher(table, plaintext):
    ciphertext = []
    i = 0
    
    while i < len(plaintext):
        c1 = plaintext[i].lower()
        c2 = plaintext[i + 1].lower() if i + 1 < len(plaintext) else 'x'
        
        if c1 == 'j':
            c1 = 'i'
        if c2 == 'j':
            c2 = 'i'
        if c1 == c2:
            c2 = 'x'
        
        row1, col1, row2, col2 = -1, -1, -1, -1
        for r in range(SIZE):
            for c in range(SIZE):
                if table[r][c] == c1:
                    row1, col1 = r, c
                if table[r][c] == c2:
                    row2, col2 = r, c
        
        if row1 == row2:
            ciphertext.append(table[row1][(col1 + 1) % SIZE])
            ciphertext.append(table[row2][(col2 + 1) % SIZE])
        elif col1 == col2:
            ciphertext.append(table[(row1 + 1) % SIZE][col1])
            ciphertext.append(table[(row2 + 1) % SIZE][col2])
        else:
            ciphertext.append(table[row1][col2])
            ciphertext.append(table[row2][col1])
        
        i += 2
    
    return ''.join(ciphertext)

def main():
    print("Tarun(192210690)")
    keyword = input("Enter keyword: ")
    plaintext = input("Enter plaintext: ")

    if len(plaintext) % 2 != 0:
        plaintext += 'x'

    table = create_table(keyword)
    ciphertext = playfair_cipher(table, plaintext)

    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
