import json
import os
import random

SAVE_FILE = "highscore.json"

# name: (max_number, max_attempts, score multiplier)
LEVELS = {
    "1": ("Easy", 50, 10, 1),
    "2": ("Medium", 100, 7, 2),
    "3": ("Hard", 500, 9, 3),
}


def load_best():
    try:
        with open(SAVE_FILE) as f:
            return json.load(f).get("best", 0)
    except (OSError, ValueError):
        return 0


def save_best(best):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump({"best": best}, f)
    except OSError:
        pass


def choose_level():
    print("\nChoose difficulty:")
    for key, (name, top, tries, mult) in LEVELS.items():
        print(f"  {key}. {name:<7} 1-{top}, {tries} attempts, x{mult} score")
    while True:
        pick = input("Level (1/2/3): ").strip()
        if pick in LEVELS:
            return LEVELS[pick]
        print("Please enter 1, 2 or 3.")


def hint(guess, target, top):
    diff = abs(guess - target)
    if diff <= top * 0.05:
        return "Very hot!"
    if diff <= top * 0.15:
        return "Warm."
    return "Cold."


def play_game():
    name, top, max_attempts, mult = choose_level()
    target = random.randint(1, top)
    attempts = 0
    low, high = 1, top

    print(f"\n{name} mode: guess a number between 1 and {top}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} "
                             f"(range {low}-{high}): "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess < 1 or guess > top:
            print(f"Enter a number between 1 and {top}.")
            continue

        attempts += 1

        if guess == target:
            score = (max_attempts - attempts + 1) * 10 * mult
            print(f"\nCorrect! The number was {target}.")
            print(f"Attempts used: {attempts} | Score: {score}")
            return score

        if guess < target:
            low = max(low, guess + 1)
            print("Too low!", hint(guess, target, top))
        else:
            high = min(high, guess - 1)
            print("Too high!", hint(guess, target, top))

    print(f"\nGame over! The number was {target}.")
    return 0


def main():
    best_ever = load_best()
    total, best, rounds = 0, 0, 0
    print("\n*** NUMBER GUESSING GAME (Phase 2) ***")
    print(f"All-time best score: {best_ever}")

    while True:
        score = play_game()
        rounds += 1
        total += score
        best = max(best, score)

        if best > best_ever:
            best_ever = best
            save_best(best_ever)
            print("New all-time high score!")

        print("\n--- STATISTICS ---")
        print(f"Rounds: {rounds} | Total: {total} | "
              f"Session best: {best} | All-time best: {best_ever}")

        again = ""
        while again not in ("y", "yes", "n", "no"):
            again = input("\nPlay again? (yes/no): ").strip().lower()
        if again.startswith("n"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
