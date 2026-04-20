import os, random, time, sys

TOP = chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)

DENSITY = 4
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    os.system("cls" if sys.platform == "win" else "clear")

while True:
    clear()

    for y in range(20):
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                print(random.choice([TOP, BOTTOM]), end="")
            else:
                print(" ", end="")
        print()

    print(FULL * 40 + "\n" + FULL * 40)
    print("Press Ctrl+C to exit.")

    time.sleep(0.2)
