import random
print('''
db   db  .d8b.  d8b   db  d888b  .88b  d88.  .d8b.  d8b   db 
88   88 d8' `8b 888o  88 88' Y8b 88'YbdP`88 d8' `8b 888o  88 
88ooo88 88ooo88 88V8o 88 88      88  88  88 88ooo88 88V8o 88 
88~~~88 88~~~88 88 V8o88 88  ooo 88  88  88 88~~~88 88 V8o88 
88   88 88   88 88  V888 88. ~8~ 88  88  88 88   88 88  V888 
YP   YP YP   YP VP   V8P  Y888P  YP  YP  YP YP   YP VP   V8P 
                                                             ''')
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
=========''']

word_list=["apple","elephant","ball"]

choice=random.choice(word_list)
live=6
placeholder=" "
word_lenght= len(choice)
for position in range(word_lenght):
    placeholder += "_ "
print(placeholder)

game_over= False
current_list=[]
while not game_over:
    guess=input("guess the latter:").lower()

    display=" "
    for letter in choice:
        if letter == guess:
            display += letter
            current_list.append(letter)
        elif letter in current_list:
            display += letter
        else:
            display += "_ "
    print(display) 
    if guess not in choice:
        live -= 1
        if live == 0:
            game_over= True
            print("you lose")
    if "_" not in display:
        game_over=True
        print("you win ")
    
    print(HANGMANPICS[live])
        
