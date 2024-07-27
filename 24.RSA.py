def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def mod_inverse(e, phi):
    print("Tarun(192210690)")
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return -1  # e is not invertible
    if t < 0:
        t += phi
    return t

def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while gcd(e, phi) != 1:
        e += 1

    # Compute d
    d = mod_inverse(e, phi)
    return n, e, d

def main():
    p = 61  # First prime number
    q = 53  # Second prime number

    # Generate RSA keys
    n, e, d = generate_keys(p, q)

    print(f"Public key: (n = {n}, e = {e})")
    print(f"Private key: (n = {n}, d = {d})")

    message = 42
    print(f"Original message: {message}")

    # Encrypt the message
    encrypted_message = mod_pow(message, e, n)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = mod_pow(encrypted_message, d, n)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
