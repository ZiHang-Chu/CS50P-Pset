def convert(str1):
    str2 = str1.replace(':)', '🙂').replace(':(', '🙁')
    return str2


def main():
    str1 = input("Please enter a smiley or frowney face: ").strip()
    print(convert(str1))


main()
