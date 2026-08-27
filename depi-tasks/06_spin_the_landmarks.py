"""
Problem: Spin the Landmarks (Arab Cultural Slot Machine)

Requirements:
1. Define a collection of landmark emoji symbols mapped to their full cultural names in a dictionary.
2. Implement a `spin()` function utilizing list comprehension and `random.choice()` to pick 3 random symbols.
3. Format output with ` | ` separators via `show_results()`.
4. Evaluate win conditions using chained equality comparisons (`check_win()`).
5. Run a 3-attempt game loop terminating immediately upon winning or exhausting attempts.

Concepts: `random.choice()`, list comprehensions, dictionary lookups, chained equality, modular functions, game loops.
"""

import random


def spin(symbols):
    return [random.choice(symbols) for _ in range(3)]


def show_results(result):
    print(" | ".join(result))


def check_win(result):
    return result[0] == result[1] == result[2]


def main():
    names = {
        "🕋": "Kaaba - Mecca",
        "🕌": "Al-Aqsa Mosque",
        "🌊": "The Nile River",
        "🏺": "Pyramids of Giza",
        "🏰": "Citadel of Salah El-Din",
        "🏛️": "Egyptian Museum - Cairo",
    }
    symbols = list(names.keys())

    print("You have 3 attempts to play!")
    counter = 0

    while True:
        input("Press Enter to spin the Arabic landmark machine... ")

        result = spin(symbols)
        show_results(result)

        if check_win(result):
            print(f"🎉 You discovered 3 of {result[0]} ({names[result[0]]})!")
            print("Cultural tour unlocked! Mabrouk!")
            break
        else:
            print("Try again to match the landmark 😄\n")

        counter += 1
        if counter == 3:
            print("You have used all 3 attempts.")
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
