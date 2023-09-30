# #1.
# def main():
#     greet = input("Greeting: ").strip().lower()
#     penalty(greet)
#
#
# def penalty(greet):
#     if greet.startswith("hello"):
#         print("$0")
#     elif greet.startswith("h"):
#         print("$20")
#     else:
#         print("$100")
def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${penalty(greeting)}")


def penalty(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


main()
