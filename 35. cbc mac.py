import copy

BLOCK_SIZE = 16

def aes_encrypt(plaintext, key):
    # Placeholder for AES encryption
    return copy.deepcopy(plaintext)

def cbc_mac(message, key):
    iv = [0] * BLOCK_SIZE
    mac = aes_encrypt(message[:BLOCK_SIZE], key)

    for i in range(BLOCK_SIZE):
        mac[i] ^= message[i]
    
    return mac

def print_mac(mac):
    for byte in mac:
        print(f"{byte:02x}", end=" ")
    print()

def main():
    print("Tarun(192210690)")
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x97, 0x20, 0x43, 0x69, 0xa5, 0x89]  # 128-bit key
    message = [0x6b, 0xc1, 0xbe, 0xe2, 0x2e, 0x40, 0x9f, 0x96, 0xe9, 0x3d, 0x7e, 0x11, 0x73, 0x93, 0x17, 0x2a]  # One-block message

    mac = cbc_mac(message, key)
    print("\nCBC MAC for one-block message:")
    print_mac(mac)

    two_block_message = message + [message[i] ^ mac[i] for i in range(BLOCK_SIZE)]
    mac = cbc_mac(two_block_message, key)
    print("CBC MAC for two-block message:")
    print_mac(mac)

if __name__ == "__main__":
    main()
