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

def get_guess(name):
    while True:
        letter = input(name + ", guess a letter: ")
        print()
        
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print(name + ", please enter a single letter.")
            print()

def display_board(solved, strikes, guesses):
    if strikes == 0:
        print("            __                                                                       ")
        print("(\,--------'()'--o                                                             \ o / ")
        print(' (_    ___    /~"                                                                |   ')
        print("  (_)_)  (_)_)                                                                  / \  ")
        
    elif strikes == 1:
        print("                      __                                                             ")
        print("          (\,--------'()'--o                                                   \ o / ")
        print('           (_    ___    /~"                                                      |   ')
        print("            (_)_)  (_)_)                                                        / \  ")

    elif strikes == 2:
        print("                                __                                                  ")
        print("                    (\,--------'()'--o                                        \ o / ")
        print('                     (_    ___    /~"                                           |   ')
        print("                      (_)_)  (_)_)                                             / \  ")

    elif strikes == 3:
        print("                                          __                                        ")
        print("                              (\,--------'()'--o                              \ o / ")
        print('                               (_    ___    /~"                                 |   ')
        print("                                (_)_)  (_)_)                                   / \  ")

    elif strikes == 4:
        print("                                                    __                              ")
        print("                                        (\,--------'()'--o                    \ o / ")
        print('                                         (_    ___    /~"                       |   ')
        print("                                          (_)_)  (_)_)                         / \  ")

    elif strikes == 5:
        print("                                                              __                    ")
        print("                                                  (\,--------'()'--o          \ o / ")
        print('                                                   (_    ___    /~"             |   ')
        print("                                                    (_)_)  (_)_)               / \  ")

    elif strikes == 6:
        print("                                                                       __           ")
        print("                                                           (\,--------'()'--o \ o / ")
        print('                                                            (_    ___    /~"    |   ')
        print("                                                             (_)_)  (_)_)      / \  ")
   

    
    print(solved)
    print("Guessed Letters: ")
    print(guesses)
    print()

def show_result(strikes, limit, name):
    if strikes >= limit:
        print(name + ", you got to pet this awesome puppy! But you still lost the game.")
        print()
    else:
        print(name + ", you win!")
        print()
        
def play_again(name):
    while True:
        result = input(name + ", do you want to play again? ").lower()
        print()
        if result in ["yes", "y"]:
            return True
        elif result in ["no", "n"]:
            credits_screen()
            return False
        else:
            print(name + ", I dont understand. Please type yes or no.")
            print()

def credits_screen(): 
    print(" __       __                      __                                  __      __          __  ______     __          __  ______    ______     __    ________ ")
    print("/  |  _  /  |                    /  |                               _/  |   _/  |        /  |/      \  _/  |        /  |/      \  /      \  _/  |  /        |")
    print("$$ | / \ $$ |  ______    _______ $$ |  ______   __    __           / $$ |  / $$ |       /$$//$$$$$$  |/ $$ |       /$$//$$$$$$  |/$$$$$$  |/ $$ |  $$$$$$$$/ ")
    print("$$ |/$  \$$ | /      \  /       |$$ | /      \ /  |  /  |          $$$$ |  $$$$ |      /$$/ $$____$$ |$$$$ |      /$$/ $$____$$ |$$$  \$$ |$$$$ |      /$$/  ")
    print("$$ /$$$  $$ |/$$$$$$  |/$$$$$$$/ $$ |/$$$$$$  |$$ |  $$ |            $$ |    $$ |     /$$/   /    $$/   $$ |     /$$/   /    $$/ $$$$  $$ |  $$ |     /$$/   ")
    print("$$ $$/$$ $$ |$$    $$ |$$      \ $$ |$$    $$ |$$ |  $$ |            $$ |    $$ |    /$$/   /$$$$$$/    $$ |    /$$/   /$$$$$$/  $$ $$ $$ |  $$ |    /$$/    ")
    print("$$$$/  $$$$ |$$$$$$$$/  $$$$$$  |$$ |$$$$$$$$/ $$ \__$$ | __        _$$ |_  _$$ |_  /$$/    $$ |_____  _$$ |_  /$$/    $$ |_____ $$ \$$$$ | _$$ |_  /$$/     ")
    print("$$$/    $$$ |$$       |/     $$/ $$ |$$       |$$    $$ |/  |      / $$   |/ $$   |/$$/     $$       |/ $$   |/$$/     $$       |$$   $$$/ / $$   |/$$/      ")
    print("$$/      $$/  $$$$$$$/ $$$$$$$/  $$/  $$$$$$$/  $$$$$$$ |$$/       $$$$$$/ $$$$$$/ $$/      $$$$$$$$/ $$$$$$/ $$/      $$$$$$$$/  $$$$$$/  $$$$$$/ $$/       ")
    print("                                               /  \__$$ |$/                                                                                                  ")
    print("                                               $$    $$/                                                                                                     ")
    print("                                                $$$$$$/                                                                                                      ")
    
def play(name):
    strikes = 0
    puzzle = get_puzzle()
    guesses = ""

    solved = get_solved(puzzle, guesses)
    display_board(solved, strikes, guesses)
    
    limit = 5
    
    while strikes <= limit and solved != puzzle:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes, guesses)

    show_result(strikes, limit, name)

repeat = True
splash_screen()
name = input("What is your name? ")
while repeat:
    play(name)
    repeat = play_again(name)

