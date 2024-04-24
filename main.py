
# for any rolledNumber == roundNumber: points += 1
# if all rolledNumbers == roundNumber


# 3 Dice are rolled, the player must match the current round number to score points.
# Rolling the current round number: 1 point per matching die.
# Rolling a "bunko" (all dice match the current round number): 21 points.

import random
import time


def checkResult(results) -> tuple[int, bool]: # POINTS, ROLL AGAIN?
    """
    Check the results of the roll and calculate the points.

    Args:
        results (list): A list of integers representing the results of the roll.

    Returns:
        tuple: A tuple containing the points earned (int) and a flag indicating whether to roll again (bool).
    """
    points: int = 0
    roll_again: bool = False

    if results.count(roundNum) == 3: # If all the results match the round number, add 21 points
        points += 21
        print('Bunko!')
    else:
        for result in results:
            if result == roundNum: # If the result matches the round number, add a point
                points += 1
                roll_again = True 

    return points, roll_again # Return the points and whether to roll again


import random

# These two functions probably could be combined into one function, but I separated them cuz reusability is king, W's in the chat


def roll() -> tuple[list[int], int, bool]: # RESULTS, POINTS, ROLL AGAIN?
    """
    Simulates rolling 3 dice and returns the results, points, and whether to roll again.

    Returns:
        tuple: A tuple containing the results of the rolls, the points earned, and a boolean indicating whether to roll again.
    """
    results: list[int] = [] # Store the results of the rolls
    # Roll 3 dice
    results.append(random.randint(1,6)) 
    results.append(random.randint(1,6)) 
    results.append(random.randint(1,6))
    
    # Return the raw results and use checkResult to determine points
    points, roll_again = checkResult(results)
    return results, points, roll_again


def singlePlayer():
    global roundNum
    roundNum = 1

    players = {'Player1': 0, 'Player2': 0, 'Player3': 0}  # Initialize the players

    # Initialize the user player
    nameInput = input('Enter your name: ')
    players[nameInput] = 0

    print(f'Round {roundNum}')
    while True:
        
        for player in players:
            if players[player] >= 21:
                print(f'{player} wins!')
                return
            scored = True
            while scored:
                if player == nameInput:
                    input(f"Press Enter for your turn, {nameInput}!")
                    result, points, roll_again = roll()
                    players[nameInput] += points
                    print(f"{nameInput}'s result: {result}, points: {points}, total points: {players[nameInput]}")
                    scored = points > 0
                else:
                    time.sleep(1)
                    result, points, roll_again = roll()
                    players[player] += points
                    print(f"{player}'s result: {result}, points: {points}, total points: {players[player]}")
                    scored = points > 0

            if players[player] >= 21:
                roundNum += 1
                print(f'Round: {roundNum}')
                print(players)
                return

        print(players)

def main():
    singlePlayer()

if __name__ == '__main__':
    main()