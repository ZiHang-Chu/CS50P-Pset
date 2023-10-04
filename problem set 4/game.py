import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            n = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < n:
                        print("Tool small!")
                    elif guess > n:
                        print("Too large!")
                    else:
                        print("Just right!")
                        raise EOFError
                except ValueError:
                    pass
        except ValueError:
            pass
        except EOFError:
            break


main()
