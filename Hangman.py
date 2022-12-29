# Created by Emma Hodor on 12/29/2022
# Art created by chrishorton (taken from hangmanwordbank.py on GitHub)

import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6
word_bank = ['lizard', 'panda', 'school', 'flower', 'lunch', 'games', 'coding', 'sweet',
             'spicy', 'water', 'college', 'artist', 'pretty', 'rainbow']

word_chosen = random.choice(word_bank)
word_chosen = [*word_chosen]

user_letters = []
for i in range(len(word_chosen)):
    user_letters.append('_')

letters_to_replace = []
incorrect_letters = []
print('Welcome to HANGMAN!')
print(HANGMANPICS[0])

pics_counter = 0

while lives > 0 and '_' in user_letters:
    print(f"Lives left: {lives}")
    print(f"Your word: {user_letters}")
    print(f"Letters NOT in word: {incorrect_letters}")
    letter = input('Choose letter: ').lower()
    if letter in word_chosen:
        for i in range(len(word_chosen)):
            if word_chosen[i] == letter:
                letters_to_replace.append(i)
        for i in letters_to_replace:
            user_letters[i] = letter
        letters_to_replace = []
        print(f"Letter {letter} in word, nice job!")
        print(HANGMANPICS[pics_counter])
    else:
        print(f"Oops! Letter {letter} is not in the word, try again.")
        pics_counter += 1
        print(HANGMANPICS[pics_counter])
        lives -= 1
        incorrect_letters.append(letter)

if lives == 0:
    print('Game over! All lives lost.')
    print(HANGMANPICS[6])

else:
    print('Congrats! You have won HANGMAN!')


