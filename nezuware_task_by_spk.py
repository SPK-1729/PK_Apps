import random

# File path for storing user data
user_data_file = 'player_data.txt'

# Initialize user credentials
user_names = []
pass_words = []

# Load existing user data from file if it exists
try:
    with open(user_data_file, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            user_names.append(username)
            pass_words.append(password)
except FileNotFoundError:
    # If file doesn't exist, continue with empty lists
    pass

print('--------------------------------')

# Save user data to the file
def save_user_data(username, password):
    with open(user_data_file, 'a') as file:
        file.write(f"{username},{password}\n")

# User registration
def signup():
    username = input("Enter your name: ")
    if username in user_names:
        print("Username already exists! Please try logging in.")
        return False
    password = input("Enter a new password: ")
    user_names.append(username)
    pass_words.append(password)
    save_user_data(username, password)
    print("Signup successful! You can now log in.")
    return True

# User login
def login():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    if username in user_names and pass_words[user_names.index(username)] == password:
        print("Let's Play!,Game On")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

# Rock, Paper, Scissors Game
def rock_paper_scissors():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter (r) for Rock, (p) for Paper, or (s) for Scissors (or 'q' to stop): ").lower()
        if user_choice == 'q':
            break
        if user_choice not in choices:
            print("Invalid choice! Please enter 'r', 'p', or 's'.")
            continue

        user_choice_full = choices[user_choice]
        computer_choice_full = random.choice(list(choices.values()))
        print(f"You chose: {user_choice_full}")
        print(f"Computer chose: {computer_choice_full}")

        if user_choice_full == computer_choice_full:
            print("It's a tie! | You got this!")
        elif (user_choice_full == 'rock' and computer_choice_full == 'scissors') or \
             (user_choice_full == 'paper' and computer_choice_full == 'rock') or \
             (user_choice_full == 'scissors' and computer_choice_full == 'paper'):
            print("You win this round! | Keep going Buddy")
            user_score += 1
        else:
            print("Computer wins this round!| Play harder,Never Quit")
            computer_score += 1

        print(f"Score -> You: {user_score}, Computer: {computer_score}")

    print("Game over! Final Score -> You:", user_score, "Computer:", computer_score)

# Tic Tac Toe Game
def tic_tac_toe():
    board = [' ' for _ in range(9)]

    def print_board():
        print("\n")
        for i in range(3):
            print("|".join(board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("-----")
        print("\n")

    def check_winner(symbol):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(board[i] == symbol for i in condition):
                return True
        return False

    def play_game():
        current_symbol = 'X'
        for turn in range(9):
            print_board()
            move = int(input(f"Player {current_symbol}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue

            board[move] = current_symbol
            if check_winner(current_symbol):
                print_board()
                print(f"Player {current_symbol} wins!")
                return

            current_symbol = 'O' if current_symbol == 'X' else 'X'

        print_board()
        print("It's a draw!")

    play_game()

# Hangman Game
def hangman():
    words = ['nezuware','python', 'java', 'hangman', 'coding', 'algorithm']
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)
    attempts = 6
    guessed_letters = set()

    while attempts > 0:
        print("\nWord to guess:", " ".join(guessed_word))
        print(f"Remaining attempts: {attempts}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print("Congratulations! You guessed the word:", word_to_guess)
                return
        else:
            attempts -= 1
            print("Incorrect guess!")

    print("Game over! The word was:", word_to_guess)

# Main menu for game selection
def main_menu():
    print("\nWelcome to the SPK Games !")
    while True:
        print("\nSelect a game to play:")
        print("1. Rock, Paper, Scissors")
        print("2. Tic Tac Toe")
        print("3. Hangman")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            tic_tac_toe()
        elif choice == '3':
            hangman()
        elif choice == '4':
            print("You are such a nice player,Come Back Soon.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Main program
def main():
    print('--- Welcome to our SPK Games ---')   
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            signup()
        elif choice == '2':
            if login():
                main_menu()
        elif choice == '3':
            print("Miss You!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
