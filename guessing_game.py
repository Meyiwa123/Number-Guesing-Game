"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random

def start_game():
  print("--------------------------------\nWelcome to the Number Guesing Game! \n--------------------------------")    
   
  highscore = 0
  game_count = 1
  play_again = "y"
  
  while play_again == "y": 
    answer = random.randint(1,10)
    number_guessed = 0
    attempts = 0
    
    if game_count >= 2:
      print("\nThe HIGHSCORE is", highscore)
  
    while number_guessed != answer:
      try:
        number_guessed = int(input("Pick a number betweeen 1 and 10: "))
        if number_guessed < 1 or number_guessed > 10:
          print("Oh no! This value is outside the range. Try again...")
        elif number_guessed > answer:
          print("It's lower! You need to guess lower.")
        elif number_guessed < answer:
          print("It's higher! You need to guess higher.")
      except ValueError:
        print("Oh no! The value entered is not a number. Try again...")
      attempts += 1
    
    if game_count == 1:
      highscore = attempts
    elif attempts != 0 and attempts < highscore:
      highscore = attempts
    
    game_count += 1
    
    print("\nYou got it! It took you", attempts, "tries.")
    play_again = input("Would you like to play again? [y]es/no: ")
    
  print("--------------------------------\n Game Over \n--------------------------------")

start_game()