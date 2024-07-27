#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to compute gcd
unsigned long gcd(unsigned long a, unsigned long b) {
    while (b != 0) {
        unsigned long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to compute modular inverse using Extended Euclidean Algorithm
unsigned long mod_inverse(unsigned long e, unsigned long phi) {
    long t = 0, newt = 1;
    long r = phi, newr = e;
    while (newr != 0) {
        long quotient = r / newr;
        long temp = t;
        t = newt;
        newt = temp - quotient * newt;
        temp = r;
        r = newr;
        newr = temp - quotient * newr;
    }
    if (r > 1) return -1;  // e is not invertible
    if (t < 0) t += phi;
    return t;
}

// Function to compute power modulo n
unsigned long mod_pow(unsigned long base, unsigned long exp, unsigned long mod) {
    unsigned long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Function to generate RSA keys
void generate_keys(unsigned long p, unsigned long q, unsigned long *n, unsigned long *e, unsigned long *d) {
    *n = p * q;
    unsigned long phi = (p - 1) * (q - 1);

    // Find e such that 1 < e < phi and gcd(e, phi) = 1
    *e = 2;
    while (gcd(*e, phi) != 1) {
        (*e)++;
    }

    // Compute d
    *d = mod_inverse(*e, phi);
}

int main() {
    unsigned long p = 61;  // First prime number
    unsigned long q = 53;  // Second prime number
    unsigned long n, e, d;

printf("Tarun(192210690)");
    generate_keys(p, q, &n, &e, &d);

    printf("Public key: (n = %lu, e = %lu)\n", n, e);
    printf("Private key: (n = %lu, d = %lu)\n", n, d);

    unsigned long message = 42;
    printf("Original message: %lu\n", message);

    // Encrypt the message
    unsigned long encrypted_message = mod_pow(message, e, n);
    printf("Encrypted message: %lu\n", encrypted_message);

    // Decrypt the message
    unsigned long decrypted_message = mod_pow(encrypted_message, d, n);
    printf("Decrypted message: %lu\n", decrypted_message);

    return 0;
}
