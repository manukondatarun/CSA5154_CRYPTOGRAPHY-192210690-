def power_mod(a, b, m):
    result = 1
    a %= m

    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1

    return result

def main():
    prime_modulus = 23
    generator = 5
    alice_secret = 6
    bob_secret = 15

    alice_public = (alice_secret * generator) % prime_modulus
    bob_public = (bob_secret * generator) % prime_modulus

    shared_secret_alice = power_mod(bob_public, alice_secret, prime_modulus)
    shared_secret_bob = power_mod(alice_public, bob_secret, prime_modulus)

    print("Tarun(192210690)")
    print(f"Shared secret key (Alice): {shared_secret_alice}")
    print(f"Shared secret key (Bob): {shared_secret_bob}")

if __name__ == "__main__":
    main()
