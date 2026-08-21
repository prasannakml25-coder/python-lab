import random


def play_game():
    print("\n===================================")
    print("       NUMBER GUESSING GAME")
    print("===================================")

    target = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    score = 0

    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        try:
            guess = int(
                input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: ")
            )

            if guess < 1 or guess > 100:
                print("Invalid number! Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < target:
                print("Too Low! Try a higher number.")

            elif guess > target:
                print("Too High! Try a lower number.")

            else:
                score = (max_attempts - attempts + 1) * 10

                print("\nCongratulations! 🎉")
                print(f"You guessed the correct number: {target}")
                print(f"Attempts used: {attempts}")
                print(f"Your score: {score}")

                return score

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print("\nGame Over!")
    print(f"The correct number was: {target}")

    return 0


def main():
    total_score = 0
    best_score = 0
    rounds = 0

    print("\n***********************************")
    print("     WELCOME TO NUMBER GUESSING")
    print("***********************************")

    while True:

        score = play_game()

        rounds += 1
        total_score += score

        if score > best_score:
            best_score = score

        print("\n===================================")
        print("          GAME STATISTICS")
        print("===================================")
        print(f"Rounds Played : {rounds}")
        print(f"Total Score   : {total_score}")
        print(f"Best Score    : {best_score}")
        print("===================================")

        while True:
            again = input(
                "\nDo you want to play another round? (yes/no): "
            ).lower().strip()

            if again == "yes" or again == "y":
                break

            elif again == "no" or again == "n":
                print("\n===================================")
                print("           FINAL RESULTS")
                print("===================================")
                print(f"Rounds Played : {rounds}")
                print(f"Total Score   : {total_score}")
                print(f"Best Score    : {best_score}")
                print("\nThank you for playing! 🎮")
                print("===================================")
                return

            else:
                print("Invalid choice! Please enter yes or no.")


if __name__ == "__main__":
    main()
