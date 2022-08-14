# Binaries on Python
# How a binary works:
# x*64 + x*32 + x*16 + x*8 + x*4 + x*2 + x*1 = Y

# Program:
# Ask to the user which binary they wish to decodify
# Decodify his choosen binary
# For each digit, put on an array
#Then make the calcs as said above

def main():
    binary = []
    decimal = ""
    operations = [64, 32, 16, 8, 4, 2, 1]
    valid = True
    inp = input("Type an binary to be decodified (7 digits, 1 and 0 only): ")

    if len(inp) != 7:
        print("Invalid binary. It had to be 7 digits long")
        main()

    for i in inp:
        binary.append(i)

    for i in binary:
        if i == "1" or i=="0":
            valid = True 
        else:
            valid = False 
            if valid == False:
                print("Invalid binary. Use only 1 and 0 (zeros).")
                main()

    for i, j in zip(binary, operations):
        decimal += f'({str(i)}*{j})+'
    else:
        decimal = list(decimal)
        decimal[-1] = ''
        decimal = ''.join(decimal)

    exec(f"print({decimal})")

main()
