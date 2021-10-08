import random
import Stages_of_Ascii_hangman
from Stages_of_Ascii_hangman import stages
end_of_game=False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives=6
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(len(chosen_word)):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game==True
            print("You loose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])