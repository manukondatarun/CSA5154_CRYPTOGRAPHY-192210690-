#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define w 32               // word size in bits
#define r 12               // number of rounds
#define b 16               // number of bytes in key
#define c (b / 4)          // number of words in key
#define t (2 * (r + 1))    // size of table S

#define P32 0xB7E15163     // Magic constant P for 32-bit word
#define Q32 0x9E3779B9     // Magic constant Q for 32-bit word

#define ROTL32(x, y) ((x << y) | (x >> (w - y)))
#define ROTR32(x, y) ((x >> y) | (x << (w - y)))

uint32_t S[t];             // Expanded key table
uint8_t L[c];              // Key

void key_expansion(uint8_t *K) {
    int i, j, s;
    uint32_t A, B;
    uint32_t L[c];

    // Initialize L
    for (i = b - 1, L[c - 1] = 0; i != -1; i--)
        L[i / 4] = (L[i / 4] << 8) + K[i];

    // Initialize S
    S[0] = P32;
    for (i = 1; i < t; i++)
        S[i] = S[i - 1] + Q32;

    // Mix key into S
    for (A = B = i = j = 0, s = 3 * ((t > c) ? t : c); s > 0; s--) {
        A = S[i] = ROTL32((S[i] + A + B), 3);
        B = L[j] = ROTL32((L[j] + A + B), (A + B));
        i = (i + 1) % t;
        j = (j + 1) % c;
    }
}

void RC5_encrypt(uint32_t *pt, uint32_t *ct) {
    uint32_t A = pt[0] + S[0];
    uint32_t B = pt[1] + S[1];
    int i;

    for (i = 1; i <= r; i++) {
        A = ROTL32((A ^ B), B) + S[2 * i];
        B = ROTL32((B ^ A), A) + S[2 * i + 1];
    }

    ct[0] = A;
    ct[1] = B;
}

void RC5_decrypt(uint32_t *ct, uint32_t *pt) {
    uint32_t A = ct[0];
    uint32_t B = ct[1];
    int i;

    for (i = r; i > 0; i--) {
        B = ROTR32((B - S[2 * i + 1]), A) ^ A;
        A = ROTR32((A - S[2 * i]), B) ^ B;
    }

    pt[0] = A - S[0];
    pt[1] = B - S[1];
}

int main() {
    uint8_t key[b] = {0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF, 
                      0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF};
    uint32_t pt[2] = {0x01234567, 0x89ABCDEF};
    uint32_t ct[2];
    uint32_t decrypted[2];

    key_expansion(key);
printf("Tarun(192210690)");
    RC5_encrypt(pt, ct);
    printf("\nEncrypted: %08x %08x\n", ct[0], ct[1]);

    RC5_decrypt(ct, decrypted);
    printf("Decrypted: %08x %08x\n", decrypted[0], decrypted[1]);

    return 0;
}
