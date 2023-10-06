
def main():
    full_text = input("Input: ").strip()
    print(f"Output: {shorten(full_text)}")


def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    change_text = ""

    for letter in text:
        if letter.lower() not in vowels:
            change_text += letter

    return change_text


if __name__ == "__main__":
    main()
