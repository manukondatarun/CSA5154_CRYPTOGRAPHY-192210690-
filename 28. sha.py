import numpy as np

BLOCK_SIZE = 1024

def initialize_state():
    return np.zeros((5, 5), dtype=np.uint64)

def sha3(message):
    state = initialize_state()
    return state

def main():
    print("Tarun(192210690)")
    message = b"Hello, world!"
    message_len = len(message)
    hash_state = sha3(message)
    
    print("SHA-3 hash:")
    for i in range(5):
        for j in range(5):
            print(f"{hash_state[i][j]:016x} ", end="")
        print()

if __name__ == "__main__":
    main()
