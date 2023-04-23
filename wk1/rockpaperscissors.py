"""
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

# accept player choices while the new game variable = true
new_game = 'yes'
while new_game == 'yes':
    player_one_choice = input("Player one choice?: ")
    player_two_choice = input("Player two choice?: ")

# calulate winner
    if player_one_choice == 'rock' and player_two_choice == 'scissors':
        winner = 'player 1'
    elif player_one_choice == 'scissors' and player_two_choice == 'paper':
        winner = 'player 1'
    elif player_one_choice == 'paper' and player_two_choice == 'rock':
        winner = 'player 1'
    else:
        winner = 'player 2'

# print the winner
    print('The winner is ' + winner + '!')
    new_game = input('Would you like to play a new game? (yes/no)')
