import random

words = {
    "apple": "A fruit that can be red or green",
    "mango": "A sweet tropical fruit, often yellow inside",
    "grape": "A small fruit that grows in bunches",
    "peach": "A soft fruit with fuzzy skin",
    "melon": "A large juicy fruit with many seeds"
}

secret_word = random.choice(list(words.keys()))
word_hint = words[secret_word]
hint_letter = random.choice(secret_word)
guessed_letters = [hint_letter]
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the hidden word.")
print("Hint:", word_hint)
print("One letter has been revealed!")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_attempts:
    print("\nWord:", end=" ")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)
else:
    print("\nGame Over! You lost!")
    print("The secret word was:", secret_word)
