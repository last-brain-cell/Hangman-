import random
import os
from time import sleep


def clear_screen():
    os.system("clear")

word = []
points = 10
temp_random_num = random.randint(0,8)
words_list = [['quiz', 'jazz', 'zinc', 'huge', 'yuck', 'vibe', 'hazy', 'salt', 'atom'], ['aqueous', 'unravel', 'peacock', 'nozzles', 'jukebox', 'keyhole', 'varying', 'buzzing', 'physics' ], ['watermelon', 'strawberry', 'friendship', 'motivation', 'cyberpunks', 'automobile', 'sacrifices', 'appreciate', 'intentions']]
intro = '''
**********************************************************************************************************************
                                                     HANGMAN
**********************************************************************************************************************
'''
outro = '''
**********************************************************************************************************************
                                               THANK YOU FOR PLAYING!
**********************************************************************************************************************
'''
wrong_word_list = []

hangman = ['''
_|_  
''','''
 |   
 |  
 |  
_|_  
''','''
 |---|
 |   
 |  
 |  
_|_  
''','''
 |---|
 |   O
 |  
 |  
_|_  
''',
'''
 |---|
 |   O
 |   |
 |  
_|_  
''',
'''
 |---|
 |   O
 |  /|
 |  
_|_  
''',
'''
 |---|
 |   O
 |  /|/
 |  
_|_  
''',
'''
 |---|
 |   O
 |  /|/
 |  / 
_|_  
''',
'''
 |---|
 |   O
 |  /|/
 |  / /
_|_  
''',]

clear_screen()

print(intro)

try: 
    start_input = input("Pls type in 'start' to start the game or quit to exit the game : ").lower()
    if start_input == 'quit':
        quit()
    else: 
        pass
    
    clear_screen()
    print(intro)

    if start_input == 'start':  
        user_choice = input("Do you want me(M) to decide the word or would you like your friend(F) to decide?: ").upper()
        if user_choice == 'M':
            level = int(input("Choose a level(1, 2, 3): "))
            secret_word = words_list[level - 1][temp_random_num]
            for i in range(0,len(secret_word)):
                word.append("_")
            clear_screen()
        elif user_choice == 'F':
            secret_word = input("Pls enter a word and make sure the player doesnt see it: ")
            for item in range(0, len(secret_word)):
                word.append("_")
        clear_screen()
        print(intro)

        list_to_str = ''.join(map(str,secret_word))      
        
        print('Start Game!')
        while points > 1:
            guess = input('''


    Take your guess: ''').lower()
            clear_screen()
            print(intro)
            print(word)
            if len(guess) > 1:
                if guess == list_to_str:
                    print("YOU WIN!!")
                    break
                else:
                    print("Your guess should contain only one letter. Pls Try again")
            else:
                if guess not in word:
                    if guess in secret_word :                   
                        answer_index = secret_word.index(guess)
                        for answer_index in (idx for idx,l in enumerate(secret_word) if l==guess):
                            word[answer_index] = guess
                            print(f'Correct!! {word}')
                        if "_" in word:
                            continue
                        else:
                            print("YOU WON!!")
                            break
                    else:
                        if guess in wrong_word_list:
                            print(f"You've already used {guess}")
                        else:
                            wrong_word_list.append(guess)
                            points -= 1
                            print(hangman[-(points)])
                            print(f'OOPS! Wrong answer, you can only make {points - 1} mistake(s) before you lose ')

                else: 
                    print("You have already got that one right, pls try something else.")

        else:                
            print("You Lost hehe ;)")
            print(f'The word was {secret_word.upper()}, Better Luck Next Time!!')
    elif start_input == 'quit':#main code
        print("You have exited from the game.")
    else:               #main code
        print("Invalid Command! Pls restart.")

    print(outro)

except KeyboardInterrupt or ValueError or TypeError:
    for i in range(5):
        print(f"Exiting game in {5 - i} seconds.")
        print("*" * (i * 4))
        sleep(1)
        os.system("clear")