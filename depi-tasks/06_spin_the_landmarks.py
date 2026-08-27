"""
Mini Project: Spin the Landmarks Slot Machine
A simple game that randomly picks 3 landmarks. The player has 3 tries to match all 3.
"""

import random


def spin(landmarks):
    result = []
    for i in range(3):
        result.append(random.choice(landmarks))

    return result


def check_result(result):
    return result[0] == result[1] == result[2]


def main():
    landmarks = ["🕋", "🕌", "🌊", "🏺", "🏰", "🏛️"]

    names = {
        "🕋": "Kaaba - Mecca",
        "🕌": "Al-Aqsa Mosque",
        "🌊": "The Nile River",
        "🏺": "Pyramids of Giza",
        "🏰": "Citadel of Salah El-Din",
        "🏛️": "Egyptian Museum - Cairo",
    }

    tries = 3

    while tries != 0:
        if tries == 1:
            print(f"{tries} spin left ")
        else:
            print(f"{tries} spins left ")

        input("Press enter to spin.. ")
        print()

        tries = tries - 1
        result = spin(landmarks)

        print(" | ".join(result))
        print()

        if check_result(result):
            print("You Won! ")
            print(f"You got free trip too {result[0]} {names[result[0]]}")
            break
        else:
            if tries >= 1:
                print("Try again")
                print()
            else:
                print("No spins left")
                print("Thanks for playing")


if __name__ == "__main__":
    main()
