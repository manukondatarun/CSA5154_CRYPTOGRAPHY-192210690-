def permute(input_val, table):
    """
    Permute the input value according to the given table.

    Args:
        input_val (int): The input value to be permuted.
        table (list): The permutation table.

    Returns:
        int: The permuted value.
    """
    result = 0
    for i, val in enumerate(table):
        result |= ((input_val >> (64 - val)) & 1) << (len(table) - 1 - i)
    return result


def des_decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the given key.

    Args:
        ciphertext (int): The ciphertext to be decrypted.
        key (int): The decryption key.

    Returns:
        int: The decrypted value.
    """
    ip_table = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv_table = [4, 1, 3, 5, 7, 2, 8, 6]

    permuted_ciphertext = permute(ciphertext, ip_table)
    decrypted = permuted_ciphertext ^ key
    decrypted = permute(decrypted, ip_inv_table)

    return decrypted


def main():
    key = 0x133457799BBCDFF1
    ciphertext = 0x0123456789ABCDEF

    decrypted = des_decrypt(ciphertext, key)

    print("Tarun(192210690)")
    print("Ciphertext: 0x{:016X}".format(ciphertext))
    print("Decrypted: 0x{:016X}".format(decrypted))

main()
