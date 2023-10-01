def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # must have 2 to 6 characters
    if not 2 <= len(s) <= 6:
        return False

    # all valid plates must start with two letters
    if not s[0:1].isalpha():
        return False

    # first number can't be 0
    first_num = True
    for letter in s:
        if letter == '0' and first_num == True:
            return False
        if letter.isdigit():
            first_num = False
            # can't have letters after numbers
        if letter.isalpha() and first_num == False:
            return False
            # no special characters allowed
        if not letter.isalpha() and not letter.isdigit():
            return False
        return True


main()
