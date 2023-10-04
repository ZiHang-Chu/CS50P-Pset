import random


def main():
    eqn = 10
    score = 0
    chance = 3
    lvl = get_level()
    while eqn > 0:
        if chance == 3:
            x, y = generate_integer(lvl)

        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                eqn -= 1
                score += 1
                # chance = 3
                continue
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            chance -= 1
            pass

        if chance == 0:
            print(f"{x} + {y} = {answer} ")
            chance = 3
            eqn -= 1
            continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
