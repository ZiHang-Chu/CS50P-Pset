def main():
    full_text = input("Input: ").strip()
    print(f"Output: {change(full_text)}")


def change(text):
    vowels = ["a", "e", "i", "o", "u"]
    change_text = ""

    for letter in text:
        if letter.lower() not in vowels:
            change_text += letter

    return change_text


main()
