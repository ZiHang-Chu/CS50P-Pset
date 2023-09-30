def main():
    str1 = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    thinking(str1)


def thinking(str1):
    # if str1 == "42" or str1 == "forty-two" or str1 == "forty two":
    #     print("Yes")
    # else:
    #     print("No")
    answers = ["42", "forty two", "forty-two"]
    if str1 in answers:
        print("Yes")
    else:
        print("No")


main()
