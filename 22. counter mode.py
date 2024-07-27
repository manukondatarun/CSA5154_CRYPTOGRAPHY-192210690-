import numpy as np

IP = [1, 5, 2, 0, 3, 7, 4, 6]
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]
EP = [3, 0, 1, 2, 1, 2, 3, 0]
P4 = [1, 3, 2, 0]
P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
P8 = [5, 2, 6, 3, 7, 4, 9, 8]
print("Tarun(192210690)")
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(input, perm):
    n = len(perm)
    output = 0
    for i in range(n):
        output |= ((input >> perm[i]) & 1) << i
    return output

def left_rotate(input, n, bits):
    return ((input << n) | (input >> (bits - n))) & ((1 << bits) - 1)

def sbox_lookup(input, sbox):
    row = ((input & 0x8) >> 2) | (input & 0x1)
    col = (input & 0x6) >> 1
    return sbox[row][col]

def f_k(input, key):
    left = input >> 4
    right = input & 0xF
    ep_output = permute(right, EP)
    xor_output = ep_output ^ key
    s0_output = sbox_lookup(xor_output >> 4, S0)
    s1_output = sbox_lookup(xor_output & 0xF, S1)
    s_output = (s0_output << 2) | s1_output
    s_output = permute(s_output, P4)
    return (left ^ s_output) << 4 | right

def generate_keys(key):
    permuted_key = permute(key, P10)
    left = permuted_key >> 5
    right = permuted_key & 0x1F
    left = left_rotate(left, 1, 5)
    right = left_rotate(right, 1, 5)
    combined = (left << 5) | right
    k1 = permute(combined, P8)
    left = left_rotate(left, 2, 5)
    right = left_rotate(right, 2, 5)
    combined = (left << 5) | right
    k2 = permute(combined, P8)
    return k1, k2

def sdes_encrypt(plaintext, key):
    ip_output = permute(plaintext, IP)
    k1, k2 = generate_keys(key)
    fk1_output = f_k(ip_output, k1)
    swapped = (fk1_output << 4) | (fk1_output >> 4)
    fk2_output = f_k(swapped, k2)
    return permute(fk2_output, IP_INV)

def sdes_decrypt(ciphertext, key):
    ip_output = permute(ciphertext, IP)
    k1, k2 = generate_keys(key)
    fk2_output = f_k(ip_output, k2)
    swapped = (fk2_output << 4) | (fk2_output >> 4)
    fk1_output = f_k(swapped, k1)
    return permute(fk1_output, IP_INV)

def ctr_encrypt_decrypt(plaintext, key, counter):
    length = len(plaintext)
    output = np.zeros(length, dtype=np.uint8)
    for i in range(length):
        keystream = sdes_encrypt(counter, key)
        output[i] = plaintext[i] ^ keystream
        counter = (counter + 1) % 256
    return output

def main():
    plaintext = [0x01, 0x02, 0x04]
    key = 0xFD  # 01111 11101
    counter = 0x00
    length = len(plaintext)

    print("Plaintext: ", end="")
    for i in range(length):
        print(f"{plaintext[i]:02X} ", end="")
    print()

    encrypted = ctr_encrypt_decrypt(plaintext, key, counter)
    print("Encrypted: ", end="")
    for i in range(length):
        print(f"{encrypted[i]:02X} ", end="")
    print()

    decrypted = ctr_encrypt_decrypt(encrypted, key, counter)
    print("Decrypted: ", end="")
    for i in range(length):
        print(f"{decrypted[i]:02X} ", end="")
    print()

if __name__ == "__main__":
    main()
