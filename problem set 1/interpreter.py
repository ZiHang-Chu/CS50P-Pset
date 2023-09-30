def main():
    x, y, z = input("Expression: ").strip().split(" ")
    print(f"{calculate(int(x), str(y), int(z)):.1f}")


def calculate(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z


main()
