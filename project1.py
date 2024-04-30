import random

def roll() :
    return random.randint(1,6)

while True :
    players = input("Enter the number of players (2-4): ")
    if players.isdigit() :
        players = int(players)
        if 2 <= players <= 4 :
            break 
        else :
            print("Must be between 2 - 4 player.")
    else :
        print("Invalid, try again")

max_score = 50

player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score :
    for player_idx in range(players) :
        print("\nPlayer number ",player_idx + 1, "turn has just started\n")
        print("Your total score is: ",player_scores[player_idx],"\n")
        current_score = 0

        while True :
            want_roll = input("Would you want to roll (y)? ")
            if want_roll.lower() != 'y' :
                break

            value = roll() 
            if value == 1 :
                current_score = 0
                print("You rolled 1 ! Turn done!")
                break
            else :
                print("You rolled: ",value)
                current_score += value
            print("Your score is: ",current_score)
            
        player_scores[player_idx] += current_score
        print("Your total score is: ",player_scores[player_idx])

max_score = max(player_scores)
wining_index = player_scores.index(max_score)
print("Player number ",wining_index + 1,"is the winner with the score of ",max_score)          