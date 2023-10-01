def main():
    case = input("camelCase: ").strip()
    print(f"snake_case: {snakecase(case)}")


def snakecase(case):
    snak = ""
    for letter in case:
        if letter.isupper():
            snak += "_"
            snak += letter.lower()
        else:
            snak += letter
    return snak


main()
