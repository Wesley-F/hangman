# Hangman
# Freshwater, Wesley

def splash_screen():
    print(" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------. ")
    print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | ")
    print("| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | | ")
    print("| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | | ")
    print("| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | | ")
    print("| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | | ")
    print("| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | | ")
    print("| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | | ")
    print("| |              | || |              | || |              | || |              | || |              | || |              | || |              | | ")
    print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | ")
    print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  ")


def get_puzzle():
    return ("wesley")
    
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
        letter = input("Guess a letter: ")
        print()
        
        if len(letter) == 1 or letter.isalpha():
            return letter

def display_board(solved):
    print(solved)
    print()

def show_result(strikes, limit):
    if strikes >= limit:
        print("You loose")
        print()
    else:
        print("You win!")
        print()
        
def play_again():
    while True:
        result = input("Do you want to play again? ").lower()
        print()
        if result in ["yes", "y"]:
            return True
        elif result in ["no", "n"]:
            return False
        else:
            print("I dont understand. Please type yes or no.")
            print()

    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6
    
    while strikes <= limit and solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(strikes, limit)

repeat = True
splash_screen()
while repeat:
    play()
    repeat = play_again()

