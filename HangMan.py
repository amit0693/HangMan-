import random
from Stages_of_Ascii_hangman import stages
end = False
fruits= ['apple','orange','banana','mango','grape','strawberry']
random_fruit = random.choice(fruits)
lives = 6
display = []
for _ in range(len(random_fruit)):
    display += "_"
while not end:
    guess = input("Guess a letter: ").lower()
    for position in range(len(random_fruit)):
        letter = random_fruit[position]
        if letter == guess:
            display[position] = letter
    if guess not in random_fruit:
        lives -= 1
        if lives == 0:
            end = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end = True
        print("You win.")
    print(stages[lives])
