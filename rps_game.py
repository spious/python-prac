import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

player_wins = 0
computer_wins = 0
game_count = 0
ties = 0

while play_again:

    playerchoice = int(input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"))

    if (playerchoice < 1 or playerchoice > 3):
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = int(random.choice("123"))

    computer = str(RPS(computerchoice)).replace("RPS.","").capitalize()
    player = str(RPS(playerchoice)).replace("RPS.","").capitalize()

    print(f'\nYou chose {player}.')
    print(f'Computer chose {computer}.\n')
   
    if (player == 1 and computer == 3):
        player_wins += 1
        print(f'Player wins! 🎉')
    elif (player == 2 and computer == 1):
        player_wins += 1
        print(f'Player wins! 🎉')
    elif (player == 3 and computer == 2):
        player_wins += 1
        print(f'Player wins! 🎉')
    elif (player == computer):
        print(f'Tie game! 🪢')
        ties += 1
    else:
        computer_wins += 1
        print('Computer wins! 🖥️')

    game_count += 1

    print(f"\nNumber of games played: {game_count}")
    print(f"Number of ties: {ties}")

    print(f"\nPlayer wins: {player_wins}")
    print(f"Python wins: {computer_wins}")
    

    play_again = input(f'\nPlay Again?? \nY for Yes \nN for No \n\n')

    if play_again.lower() not in ['y','n']:
        play_again = input(f'\nPlease enter either \nY for Yes \nN for No \n\n')
    elif play_again.lower() == 'y':
        continue
    else:
        print(f'\nThank You for Playing!👋')
        play_again = False