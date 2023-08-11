#Step 3

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6
end_of_game=False
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(len(stages))
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.



while not end_of_game:
        print(lives) 
        guess = input("Guess a letter: ").lower()
        
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
          
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            print(stages[lives])
            lives-=1
        if lives==0:
            print("no lives remaining")
            end_of_game=True
                
        print(display)     
        if "_" not in display:
            print("you won")      
        
print(stages[lives])
print("you lose")
