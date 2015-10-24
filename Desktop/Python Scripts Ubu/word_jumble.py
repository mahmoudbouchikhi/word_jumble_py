# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
from gi.overrides.keysyms import j

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
vocabulary = ("program", "goggle", "not difficult", "after a question", "phone")
hint=""
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
[WORDS]=[vocabulary]



# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != "hint":
    if guess != correct:
        print("Sorry, that's not it. and remember that you can get help at anytime by typing hint")
        guess = input("Your guess: ")

    elif guess == correct:
        print("That's it!  You guessed it!\n")
        print("Thanks for playing.")
else :

        i=j
        print(j)


input("\n\nPress the enter key to exit.")
###
def hint(WORDS, vocabulary):
    count = 0

#    for i in WORDS:
#        return vocabulary