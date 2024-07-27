def main():
    p8 = [6, 7, 8, 9, 1, 2, 3, 4]
    p10 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    print("Tarun(192210690)")
    input_bits = input("Enter 10 bits input: ")
    if len(input_bits) != 10:
        print("Input must be exactly 10 bits.")
        return

    temp = [''] * 10
    for i in range(10):
        cnt = p10[i]
        temp[i] = input_bits[cnt - 1]

    print("\nYour p10 key is    :")
    print(",".join(map(str, p10)))

    print("Bits after p10     :")
    print("".join(temp))
    
    # LS-1 operation
    temp = temp[1:5] + temp[:1] + temp[6:10] + temp[5:6]

    print("Output after LS-1  :")
    print("".join(temp))

    print("\nYour p8 key is     :")
    print(",".join(map(str, p8)))
    
    k1 = [''] * 8
    for i in range(8):
        cnt = p8[i]
        k1[i] = temp[cnt - 1]

    print("Your key k1 is     :")
    print("".join(k1))

if __name__ == "__main__":
    main()
