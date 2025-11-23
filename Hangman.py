import random
 
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        update_display += 1
    x = 0
 
 
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
 
word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud", "python", "hangman", "chal lenge", "monitor","x-ray", "death", "murder", "blood", "rotten", "hell", "demon", "monster", "dying", "end", "mortality", "demise", "passing", "afterlife", "departed", "destruction", "apocalypse", "dangerous", "extinct", "extermination", "fatality", "fallen", "gone", "killing", "grim reaper", "killer", "destroyer", "loner", "murderer", "graveyard", "century", "torture", "2025", "2012", "@sakshaat", "johan", "subaru", "wine", "bomb", "psychopath", "psycho killer", "gangster", "ajay pratap singh", "mohit", "tanishq", "die", "disease", "pandemic", "virus", "infection", "Problems", "misery", "dooms day", "apocalypse"]
 
chosen_word = list(random.choice(word_list))
 
blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
 
update_display = 0
 
#----------------------------------------------------------------------------------------------
 
print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print("GAME OVER.")
    
