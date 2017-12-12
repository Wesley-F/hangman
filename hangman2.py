# Hangman
# Freshwater, Wesley

import os
import random

def splash_screen():
    with open("art/start_screen.txt", 'r') as f:
        lines = f.read()
        print(lines)


def get_puzzle():
    path = "data"

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        with open(path + "/" + file_names[i], 'r') as f:
            lines = f.read().splitlines()
            category = lines[0]
            
        print(str(i + 1) + ") " + category)

    choice = input('pick one ')
    choice = int(choice) - 1

    file = path + "/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()


    category_name = lines[0]
    puzzle = random.choice(lines[1:])

    print(category_name)
    return puzzle

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
        
        if len(letter) == 1 and letter.isalpha() or letter == " ":
            return letter
        else:
            print(name + ", please enter a single letter.")
            print()

def display_board(solved, strikes, guesses):
    if strikes == 0:
        with open("art/0.txt", 'r') as f:
            lines = f.read()
            print(lines)
        
    elif strikes == 1:
        with open("art/1.txt", 'r') as f:
            lines = f.read()
            print(lines)

    elif strikes == 2:
        with open("art/2.txt", 'r') as f:
            lines = f.read()
            print(lines)

    elif strikes == 3:
        with open("art/3.txt", 'r') as f:
            lines = f.read()
            print(lines)  

    elif strikes == 4:
        with open("art/4.txt", 'r') as f:
            lines = f.read()
            print(lines)

    elif strikes == 5:
        with open("art/5.txt", 'r') as f:
            lines = f.read()
            print(lines) 

    elif strikes == 6:
        with open("art/6.txt", 'r') as f:
            lines = f.read()
            print(lines)  
   

    
    print(solved)
    print("Guessed Letters: ")
    print(guesses)
    print()

def show_result(strikes, limit, name, puzzle):
    if strikes >= limit:
        print(name + ", you got to pet this awesome puppy! But you still lost the game.")
        print()
        print("The word was " + puzzle + "!")
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
    with open("art/credits.txt", 'r') as f:
        lines = f.read()
        print(lines)
        
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

    show_result(strikes, limit, name, puzzle)

repeat = True
splash_screen()
name = input("What is your name? ")
while repeat:
    play(name)
    repeat = play_again(name)

