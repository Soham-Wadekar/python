# 8. Develop a simple number guessing game where the user has to guess a randomly generated number within a specified range.

import random


def choose_num(range=[0, 1], impossible=False):
    if impossible:
        return random.random()
    else:
        start, end = min(range), max(range)
        return random.randint(start, end)


def user_guess(range=[0, 1], impossible=False):
    if impossible:
        user_input = float(input(f"Guess the number from {range}: "))
    else:
        user_input = int(input(f"Guess the number from {range}: "))

    return user_input


def is_correct(usr_guess, comp_guess):
    if usr_guess == comp_guess:
        print("You are correct!")
    else:
        print(f"Nope! The number was {comp_guess}")


difficulty = input(
    "Choose Difficulty: \nA. Baby\nB. Easy\nC. Intermediate\nD. Hard\nE. Impossible\nChoose: "
)

match difficulty:
    case "A":
        range = [1, 2]
        result = choose_num(range)
        guess = user_guess(range)
        is_correct(guess, result)
    case "B":
        range = [1, 10]
        result = choose_num(range)
        guess = user_guess(range)
        is_correct(guess, result)
    case "C":
        range = [1, 25]
        result = choose_num(range)
        guess = user_guess(range)
        is_correct(guess, result)
    case "D":
        range = [1, 100]
        result = choose_num(range)
        guess = user_guess(range)
        is_correct(guess, result)
    case "E":
        result = choose_num(impossible=True)
        guess = user_guess(impossible=True)
        is_correct(guess, result)
