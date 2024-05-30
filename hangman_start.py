import random

words = ["marriage", "love", "cayla"]
chosen_word = random.choice(words)
print(f'the chosen word is {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

guess = input('Guess a letter: ').lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess
print(display)