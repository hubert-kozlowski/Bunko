
# for any rolledNumber == roundNumber: points += 1
# if all rolledNumbers == roundNumber


# 3 Dice are rolled, the player must match the current round number to score points.
# Rolling the current round number: 1 point per matching die.
# Rolling a "bunko" (all dice match the current round number): 21 points.

import random
import time


def checkResult(results):  # Check the results of the roll
    points = 0
    roll_again = False
    if results.count(roundNum) == 3:  # Check if all dice match the round number
        points += 21
        print('Bunko!')
    else:  # If not, check if any dice match the round number
        for result in results: 
            if result == roundNum: 
                points += 1
                roll_again = True
    return points, roll_again


def roll():
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