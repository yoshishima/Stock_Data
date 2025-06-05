# Code from kuatroka: https://github.com/kuatroka

def get_cusip9(cusip8):
    # Validate that input is a string of exactly 8 characters
    if not isinstance(cusip8, str) or len(cusip8) != 8:
        print("invalid CUSIP: input must be exactly 8 characters")
        exit()

    sum = 0
    for i in range(1, 9):
        c = cusip8[i - 1]
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            p = ord(c.lower()) - 96
            v = p + 9
        elif c == "*":
            v = 36
        elif c == "@":
            v = 37
        elif c == "#":
            v = 38
        else:
            print("Invalid CUSIP: Invalid Character Encountered")
            exit()

        if i % 2 == 0:
            v *= 2

        sum = sum + (v // 10) + (v % 10)

    check_digit = (10 - (sum % 10)) % 10
    return cusip8 + str(check_digit)


def main():
    cusip8 = input("Enter 8-character CUSIP: ")
    cusip9 = get_cusip9(cusip8)
    print("9-character CUSIP:", cusip9)


if __name__ == "__main__":
    main()
