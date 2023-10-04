import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]


def main():
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlietize("Input: ", font)
    elif len(sys.argv) == 3 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        figlietize("Input: ", sys.argv[2])
    else:
        sys.exit("Invalid usage")


def figlietize(prompt, f):
    text = input(prompt)
    figlet.setFont(font=f)
    print("Output: ")
    print(figlet.renderText(text))


main()
