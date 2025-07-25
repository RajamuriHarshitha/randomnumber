import random

def calculator():
    print("\n--- Basic Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", num1 + num2)
        elif choice == '2':
            print("Result: ", num1 - num2)
        elif choice == '3':
            print("Result: ", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error: Cannot divide by zero")
    else:
        print("Invalid Input")


def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Guess a number between 1 and 100. You have 10 attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess == number_to_guess:
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
                break
            elif abs(guess - number_to_guess) <= 5:
                print("🔥 Very close!")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"\n❌ Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")


# --- Main Menu ---
def main():
    while True:
        print("\n=== Task Menu ===")
        print("1. Calculator")
        print("2. Number Guessing Game")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            number_guessing_game()
        elif choice == '3':
            print("Thank you! Exiting program.")
            break
        else:
            print("Invalid choice. Please select again.")

main()

