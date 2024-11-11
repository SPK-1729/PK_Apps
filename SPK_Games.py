import random
# Define initial usernames and passwords (can be empty if file doesn't exist)
# so if you are using this program then go for signup 
user_names = []
pass_words = []
# File path for storing user data
user_data_file = 'user_data.txt'
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
print('--- Welcome to our SPK webpage ---')
# Function for login
def pk_login():
    while True:
        # Get user input
        username_input = input('Enter your username: ').strip()

        # Check if username exists
        if username_input not in user_names:
            print('!!!Username not found!!!')
            choice = input('Enter 1 to sign up or 2 to try again with a different username: ').strip()
            if choice == '1':
                return False, True  # Return False to indicate login failure and True to indicate signup request
            elif choice == '2':
                continue  # Retry login with a different username
            else:
                print('Invalid choice. Please enter 1 or 2.')
        else:
            password_input = input('Enter your password: ').strip()
            # Check if password matches for the entered username
            if password_input == pass_words[user_names.index(username_input)]:
                print('Login successful!')
                return True, False  # Return True to indicate login success and False for no signup request
            else:
                print('Invalid password. Please try again.')
# Function for signup
def pk_signup():
    while True:
        # Get user input
        new_username = input('Enter a new username: ').strip()
        # Validate if username already exists
        if new_username in user_names:
            print('Username already exists. Please choose a different username.')
        else:
            new_password = input('Enter a new password: ').strip()
            # Add new username and password to lists
            user_names.append(new_username)
            pass_words.append(new_password)
            # Save updated user data to file
            with open(user_data_file, 'a') as file:
                file.write(f'{new_username},{new_password}\n')
            # Determine the number of users
            num_users = len(user_names)
            if num_users == 1:
                print(f'Congratulations! You are our 1st user, {new_username}. Welcome to the family!')
            else:
                print(f'Congratulations! You are our {num_users}th user, {new_username}. Welcome to the family!')
            return True  # Return True to indicate signup success
# Game: Guess the Number
def guess_the_number():
    target_number = random.randint(1, 100)
    attempts_left = 5
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    while attempts_left > 0:
        print(f"Attempts left: {attempts_left}")
        try:
            guess = int(input("Guess the number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number '{target_number}' correctly.")
            return
        attempts_left -= 1
    print(f"Sorry, you ran out of attempts. The number was '{target_number}'.")
# Game: Tic-Tac-Toe
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    winner = None
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns marking spaces in a 3x3 grid.")
    print("Player 'X' goes first.")
    print("Enter row (0, 1, 2) and column (0, 1, 2) to make your move.")
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 9)
    def check_winner(board, player):
        for i in range(3):
            if all([board[i][j] == player for j in range(3)]) or \
               all([board[j][i] == player for j in range(3)]) or \
               (board[0][0] == board[1][1] == board[2][2] == player) or \
               (board[0][2] == board[1][1] == board[2][0] == player):
                return True
        return False
    print_board(board)
    while True:
        player = players[turn % 2]
        print(f"Player {player}, it's your turn.")
        try:
            row = int(input("Enter row (0, 1, 2): ").strip())
            col = int(input("Enter column (0, 1, 2): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        print_board(board)
        if check_winner(board, player):
            winner = player
            break
        if all([cell != " " for row in board for cell in row]):
            break
        turn += 1
    if winner:
        print(f"Congratulations! Player {winner} wins!")
    else:
        print("It's a draw!")
# Game: Rock, Paper, Scissors
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose: rock, paper, or scissors.")

    player_choice = input("Enter your choice: ").strip().lower()
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")
# Game: Dice Rolling Simulator
def dice_rolling_simulator():
    num_dice = int(input("Enter number of dice to roll: ").strip())
    num_rolls = int(input("Enter number of rolls: ").strip())
    print(f"Rolling {num_dice} dice {num_rolls} times...")
    for roll in range(1, num_rolls + 1):
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        print(f"Roll {roll}: {rolls}, Total: {sum(rolls)}")
# Game: Coin Toss
def coin_toss():
    print("Welcome to Coin Toss!")
    print("Guess heads or tails.")
    player_guess = input("Enter your guess (heads or tails): ").strip().lower()
    coin = random.choice(['heads', 'tails'])
    print(f"Coin toss result: {coin}")
    if player_guess == coin:
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, you guessed incorrectly.")
# Main program loop
while True:
    choice = input('Please enter your choice:\n1. Login\n2. Signup\n3. Exit\n').strip()
    if choice == '1':
        login_result, signup_requested = pk_login()
        if login_result:
            # After successful login, offer game selection
            while True:
                game_choice = input('Select a game:\n1. Guess the Number\n2. Tic-Tac-Toe\n3. Rock, Paper, Scissors\n4. Dice Rolling Simulator\n5. Coin Toss\n6. Logout\n').strip()
                if game_choice == '1':
                    guess_the_number()
                elif game_choice == '2':
                    tic_tac_toe()
                elif game_choice == '3':
                    rock_paper_scissors()
                elif game_choice == '4':
                    dice_rolling_simulator()
                elif game_choice == '5':
                    coin_toss()
                elif game_choice == '6':
                    print('Logging out...')
                    break
                else:
                    print('Invalid choice. Please enter a number between 1 and 6.')
            break  # Exit login loop after logging out
        elif signup_requested:
            signup_result = pk_signup()
            if signup_result:
                continue  # Retry login after successful signup
            else:
                print('Returning to login.')
    elif choice == '2':
        signup_result = pk_signup()
        if signup_result:
            # After successful signup, offer game selection
            while True:
                game_choice = input('Select a game:\n1. Guess the Number\n2. Tic-Tac-Toe\n3. Rock, Paper, Scissors\n4. Dice Rolling Simulator\n5. Coin Toss\n6. Logout\n').strip()
                if game_choice == '1':
                    guess_the_number()
                elif game_choice == '2':
                    tic_tac_toe()
                elif game_choice == '3':
                    rock_paper_scissors()
                elif game_choice == '4':
                    dice_rolling_simulator()
                elif game_choice == '5':
                    coin_toss()
                elif game_choice == '6':
                    print('Logging out...')
                    break
                else:
                    print('Invalid choice. Please enter a number between 1 and 6.')
            break  # Exit signup loop after logging out
    elif choice == '3':
        print('Exiting program. Have a good day and sign up later!')
        break
    else:
        print('Invalid choice. Please enter 1, 2, or 3.')
# Continue with your application logic after successful login
