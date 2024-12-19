import random

word_list = ["pineapple", "kiwi", "strawberry", "cherry", "blackberry"]

print(word_list)

word = random.choice(word_list)

print(word)


def ask_for_input():
    while True:
        guess = input("please enter a single letter ")

        if len(guess) == 1 and guess.isalpha():
            return guess.lower()

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


check_guess("a")

ask_for_input()


