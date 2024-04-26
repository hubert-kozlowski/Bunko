
# for any rolledNumber == roundNumber: points += 1
# if all rolledNumbers == roundNumber


# 3 Dice are rolled, the player must match the current round number to score points.
# Rolling the current round number: 1 point per matching die.
# Rolling a "bunko" (all dice match the current round number): 21 points.


import random
import time
import tkinter as tk


def checkResult(results): # POINTS, ROLL AGAIN?
    """
    Check the results of the roll and calculate the points.

    Args:
        results (list): A list of integers representing the results of the roll.

    Returns:
        tuple: A tuple containing the points earned (int) and a flag indicating whether to roll again (bool).
    """
    points: int = 0

    if results.count(roundNum) == 3: # If all the results match the round number, add 21 points
        points += 21
        print('BUNKO')
    elif results[0] == results[1] == results[2] and results[0] != roundNum: # If all 3 have the same number but don't match the round number, add 5 points
        points += 5
    else:
        for result in results:
            if result == roundNum: # If the result matches the round number, add a point
                points += 1




    return points # Return the points and whether to roll again

# These two functions probably could be combined into one function, but I separated them cuz reusability is king, W's in the chat


def roll(): # RESULTS, POINTS, ROLL AGAIN?
    """
    Simulates rolling 3 dice and returns the results, points, and whether to roll again.

    Returns:
        tuple: A tuple containing the results of the rolls, the points earned, and a boolean indicating whether to roll again.
    """
    results = [] # Store the results of the rolls
    # Roll 3 dice
    results.append(random.randint(1,6)) 
    results.append(random.randint(1,6)) 
    results.append(random.randint(1,6))
    
    # Return the raw results and use checkResult to determine points
    points = checkResult(results)
    return results, points


def singleplayer():

    global roundNum
    roundNum = 1
    maxRound = 4

    players = {'Player1': 0, 'Player2': 0, 'Player3': 0}  # Initialize the players
    winners = {}  # Initialize the winners

    # Initialize the user player
    nameInput = input('Enter your name: ')
    players[nameInput] = 0

    print(f'\033[95mRound: {roundNum}\033[0m')
    while roundNum < maxRound:
        print(f'Current scores: {players}')
        print('-'*20)
        for player in players:
            scored = True

            while scored: # Keep rolling until the player doesn't score
                if player == nameInput:
                    if players[nameInput] >= 21:
                        break # If the player has already scored 21 points, end the round
                    input(f"Press Enter for your turn, {nameInput}!")
                    result, points = roll()
                    players[nameInput] += points
                    print(f"\033[94m{nameInput}'s result: {result}, points: {points}, total points: {players[nameInput]}\033[0m") # Print USER results in blue
                    scored = points > 0

                else: # AI players
                    if players[player] >= 21:
                        break 
                    time.sleep(1)
                    result, points = roll()
                    players[player] += points
                    print(f"{player}'s result: {result}, points: {points}, total points: {players[player]}") # Print AI results in white
                    scored = points > 0



            # If the player gets a Bunko, reset the scores and increment the round       
            if players[player] >= 21:
                print(f"\033[92m{player} WON THE ROUND!\033[0m")
                print(f'Round {roundNum} is over!')
                print('-'*20)
                for key in players: # Reset player scores and increment round number
                    players[key] = 0

                # keep track of the winners, and how many times they won
                if player in winners:
                    winners[player] += 1
                else:
                    winners[player] = 1
                roundNum += 1
                
                if roundNum < maxRound:
                    print(f'\033[95mRound: {roundNum}\033[0m')
                break

    print(f'People who won: {winners}')
    print(f'Overall Winner: {max(winners, key=winners.get)}')










def simulation():
    global roundNum
    roundNum = 1
    maxRound = 7 

    players = {'Player1': 0, 'Player2': 0, 'Player3': 0, 'Player4': 0}  # Initialize the players
    winners = {}  # Initialize the winners

    print(f'\033[95mRound: {roundNum}\033[0m')  # Print the round number here
    while roundNum < maxRound:
        
        print(f'Current scores: {players}')
        print('-'*20)
        for player in players:
            scored = True

            while scored: # Keep rolling until the player doesn't score
                if players[player] >= 21:
                    break 
                result, points = roll()
                players[player] += points
                print(f"{player}'s result: {result}, points: {points}, total points: {players[player]}") # Print AI results in white
                scored = points > 0

            # If the player gets a Bunko, reset the scores and increment the round       
            if players[player] >= 21:
                print(f"\033[92m{player} WON THE ROUND\033[0m")
                print(f'Round {roundNum} is over!')
                print('-'*20)

                # Reset player scores
                for key in players:
                    players[key] = 0

                # Keep track of the winners, and how many times they won
                if player in winners:
                    winners[player] += 1
                else:
                    winners[player] = 1
                roundNum += 1

                if roundNum < maxRound:
                    print(f'\033[95mRound: {roundNum}\033[0m')
                break

    print(f'People who won: {winners}')
    print(f'Overall Winner: {max(winners, key=winners.get)}')



        

def main():
    simulation()

if __name__ == '__main__':
    main()


