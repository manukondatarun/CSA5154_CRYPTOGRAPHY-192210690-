import struct
print("Tarun(192210690)")
# Constants
w = 32                # word size in bits
r = 12                # number of rounds
b = 16                # number of bytes in key
c = b // 4            # number of words in key
t = 2 * (r + 1)       # size of table S

P32 = 0xB7E15163      # Magic constant P for 32-bit word
Q32 = 0x9E3779B9      # Magic constant Q for 32-bit word

# Helper Functions
def ROTL(x, y):
    return ((x << y) & 0xFFFFFFFF) | (x >> (32 - y))

def ROTR(x, y):
    return (x >> y) | ((x << (32 - y)) & 0xFFFFFFFF)

def key_expansion(K):
    L = [0] * c
    for i in range(b - 1, -1, -1):
        L[i // 4] = (L[i // 4] << 8) + K[i]

    S = [P32]
    for i in range(1, t):
        S.append((S[i - 1] + Q32) & 0xFFFFFFFF)

    i = j = 0
    A = B = 0
    for _ in range(3 * max(t, c)):
        A = S[i] = ROTL((S[i] + A + B) & 0xFFFFFFFF, 3)
        B = L[j] = ROTL((L[j] + A + B) & 0xFFFFFFFF, (A + B) % 32)
        i = (i + 1) % t
        j = (j + 1) % c

    return S

def RC5_encrypt(pt, S):
    A, B = pt
    A = (A + S[0]) & 0xFFFFFFFF
    B = (B + S[1]) & 0xFFFFFFFF
    for i in range(1, r + 1):
        A = (ROTL((A ^ B), B % 32) + S[2 * i]) & 0xFFFFFFFF
        B = (ROTL((B ^ A), A % 32) + S[2 * i + 1]) & 0xFFFFFFFF
    return A, B

def RC5_decrypt(ct, S):
    A, B = ct
    for i in range(r, 0, -1):
        B = (ROTR((B - S[2 * i + 1]) & 0xFFFFFFFF, A % 32) ^ A) & 0xFFFFFFFF
        A = (ROTR((A - S[2 * i]) & 0xFFFFFFFF, B % 32) ^ B) & 0xFFFFFFFF
    A = (A - S[0]) & 0xFFFFFFFF
    B = (B - S[1]) & 0xFFFFFFFF
    return A, B

# Main Function
def main():
    key = [0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF,
           0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF]
    pt = (0x01234567, 0x89ABCDEF)

    S = key_expansion(key)

    ct = RC5_encrypt(pt, S)
    print("Encrypted: {:08x} {:08x}".format(ct[0], ct[1]))

    decrypted = RC5_decrypt(ct, S)
    print("Decrypted: {:08x} {:08x}".format(decrypted[0], decrypted[1]))

if __name__ == "__main__":
    main()
