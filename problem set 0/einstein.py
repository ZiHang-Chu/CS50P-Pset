def convert(m):
    e = m * (300000000 ** 2)
    return e


def main():
    m = input("Enter a mass in kilograms: ").strip()
    print("E:", convert(int(m)))


main()
