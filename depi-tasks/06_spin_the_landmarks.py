"""
Problem: Slot-Machine Game - Spin the Landmarks (لعبة سحب لأشهر معالم الوطن العربي)

Requirements:
1. Define a pool of landmark symbols (emojis) and a lookup dictionary mapping each symbol to its cultural name.
2. Implement a `spin()` function that randomly selects 3 symbols using the `random` module.
3. Implement a win-condition check (`check_result()`) verifying if all 3 spun symbols match (`symbol1 == symbol2 == symbol3`).
4. Manage a game loop giving the player exactly 3 attempts to win:
   - Provide clear countdown messaging with proper singular/plural grammar ("1 spin left" vs "X spins left").
   - If won: Announce the victory, display the landmark name from the dictionary, and terminate the game.
   - If lost: Prompt the user to retry while spins remain, or display a game-over message when out of spins.

Concepts: `random.choice()`, chained comparisons (`a == b == c`), dictionary key lookup, while loop state tracking, entry-point modularity (`if __name__ == '__main__'`).
"""

import random


def spin(landmarks):
    result = []
    for _ in range(3):
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
            print(f"{tries} spin left")
        else:
            print(f"{tries} spins left")

        input("Press enter to spin.. ")
        print()

        tries = tries - 1
        result = spin(landmarks)

        print(" | ".join(result))
        print()

        if check_result(result):
            print("You Won! 🎉")
            print(f"You got a free trip to {result[0]} ({names[result[0]]})!")
            break
        else:
            if tries >= 1:
                print("Try again 😄\n")
            else:
                print("No spins left.")
                print("Thanks for playing! Have a nice day!\n")


if __name__ == "__main__":
    main()
