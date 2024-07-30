# Function to find modular inverse of a under modulo m
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to decrypt the ciphertext
def decrypt_affine_cipher(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv == -1:
        print(f"No modular inverse exists for a={a}")
        return

    decrypted_text = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            y = ord(char) - ord('A')
            x = (a_inv * (y - b + 26)) % 26
            decrypted_text += chr(x + ord('A'))
        else:
            decrypted_text += char
    print(decrypted_text)

def main():
    print("Tarun(192210690)")
    ciphertext = "BPU..."
    x1, y1 = 4, 1  # E -> B
    x2, y2 = 19, 20  # T -> U

    for a in range(1, 26):
        if mod_inverse(a, 26) == -1:
            continue
        b = (y1 - a * x1) % 26
        if b < 0:
            b += 26

        y_check = (a * x2 + b) % 26
        if y_check == y2:
            print(f"Possible keys: a = {a}, b = {b}")
            print("Decrypted message: ", end="")
            decrypt_affine_cipher(ciphertext, a, b)
            break

if __name__ == "__main__":
    main()
