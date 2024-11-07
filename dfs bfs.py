import random

def alpha_beta_guess(low, high, depth, alpha, beta, maximizing):
    if low > high:
        return None

    if depth == 0:
        return random.randint(low, high)

    if maximizing:
        best_guess = low
        for guess in range(low, high + 1):
            result = alpha_beta_guess(guess + 1, high, depth - 1, alpha, beta, False)
            if result is not None:
                best_guess = max(best_guess, result)
                alpha = max(alpha, best_guess)
                if beta <= alpha:
                    break
        return random.randint(low, high)
    else:
        best_guess = high
        for guess in range(low, high + 1):
            result = alpha_beta_guess(low, guess - 1, depth - 1, alpha, beta, True)
            if result is not None:
                best_guess = min(best_guess, result)
                beta = min(beta, best_guess)
                if beta <= alpha:
                    break
        return random.randint(low, high)

def guess_the_number():
    number = random.randint(1, 100)
    user_attempts = 0
    ai_attempts = 0
    max_attempts = 10

    ai_low = 1
    ai_high = 100

    print("Welcome to Guess the Number!")
    print("You and the AI will take turns guessing the number between 1 and 100.")
    print(f"Each has {max_attempts} total attempts to guess the correct number.")

    while user_attempts < max_attempts and ai_attempts < max_attempts:
        print("\nYour turn:")
        try:
            user_guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")
            continue
        user_attempts += 1

        if user_guess < number:
            print("Too low!")
        elif user_guess > number:
            print("Too high!")
        else:
            print(f"\nCongratulations! You guessed the number in {user_attempts} attempts. You win!")
            return

        print("\nAI's turn:")
        ai_guess = alpha_beta_guess(ai_low, ai_high, depth=5, alpha=-float('inf'), beta=float('inf'), maximizing=True)
        if ai_guess is None:
            ai_guess = random.randint(ai_low, ai_high)
        ai_attempts += 1
        print(f"AI guessed: {ai_guess}")

        if ai_guess < number:
            print("AI's guess is too low!")
            ai_low = ai_guess + 1
        elif ai_guess > number:
            print("AI's guess is too high!")
            ai_high = ai_guess - 1
        else:
            print(f"\nAI guessed the number in {ai_attempts} attempts. AI wins!")
            return

    print("\nNeither you nor the AI guessed the number within 10 attempts. Game over!")

def menu():
    while True:
        choice = input("\n1. Play Guess the Number\n2. Exit\nEnter your choice: ")
        if choice == '1':
            guess_the_number()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    menu()
