from mimetypes import guess_extension
from multiprocessing.sharedctypes import Value
import random
from tracemalloc import start



ranges = list(range(1,11))
high_scores = []

def start_game():
    start_over = 'yes'
    print('Welcome to the Guessing Game!')


    # 1. Display an intro/welcome message to the player.``
    try: 
        person_name = input("Hello there! May I have your name?! ")
        
        if person_name.isalpha() == False:
            print("Please try again, letters only")
            start_game()
            return 
            
    except TypeError as err:
        print(err)
        
    coregame()    

    

    while(start_over.lower() == 'yes'): 
        try:
            start_over = input("Would you like to play again? Yes/No: ")

            if start_over.lower() != 'yes' and start_over.lower() != 'no':
                start_over = 'yes'
                print("Please submit Yes or No only")
                continue

        except ValueError as err:
            print(err)
                
        else:
            if start_over.lower() == 'yes':
                print(f"Alright, {person_name} try to beat your last high score of: "  + str(min(high_scores)))
                coregame()

            elif min(high_scores) == 0:
                print("You got the right answer on the first try! Do you want to test your luck again?!")    
            else:
                
                print(f"{person_name} your high score is: "  + str(min(high_scores)))
                print(f'Thank you for playing {person_name}. Goodbye!') 
                break          
    # 5. Let the player know the game is ending, or something that indicates the game is over.

    

def coregame():
    guesses = 0
    finalscore = 0

    num_provided = 0 # 8
    random_num = random.randint(1,10) 

    while (num_provided != random_num):     
        try:
            num_provided = int(input("Pick a number between 1- 10:  "))
        
        except ValueError as err:
            print("You did not input a number, please try again.")
        
        else:
            guesses +=1
            
            if num_provided not in ranges:
                print("You did not provide a guess with the range provided, please try again")
                continue

            if num_provided > random_num:
                print("It's lower")
                # go back to num_provided to repeat process
            
            elif num_provided < random_num:
                print("It's higher")
                # go back to num_provided to repeat process
            
            elif num_provided == random_num:
                print("You got it! The answer is correct. This round is now over.")
                # 4. Once the guess is correct, stop looping, inform the user they "Got it" 
                # print(f'Its taken', guesses, ' tries to reach the correct number')    
                # return None

    print(f"Your last score was " + str(guesses) + " try to beat it!")

    high_scores.append(guesses)

                # set the value of guesses guesses to highscore
    # elif high_score < guesses: ## we don't need it because we aren't doing with it. 
    # # set keep value of high score

start_game()