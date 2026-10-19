def ask_choice():
    # Function to ask the player for their choice and validate it
    global player_choice
    player_choice = int(input('Please choose rock paper or scissors.(1/2/3) respectively'))
    if player_choice == 1 or player_choice == 2 or player_choice == 3:
        computer_random_choice()
    else:
        print('Wrong input')
        print('Please try again')
        ask_choice()


def computer_random_choice():
    # Function to generate a random choice for the computer
    import random
    global computer_choice
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print("The computer chose rock")
    elif computer_choice == 2:
        print('The computer chose paper')
    else:
        print('The computer chose scissors')

def player_win_loss():
    # Function to determine if the player wins, loses, or ties
    global player_result
    if computer_choice == 1 and player_choice == 2:
        player_result = 1
    elif computer_choice == 2 and player_choice == 3:
        player_result = 1
    elif computer_choice == 3 and player_choice == 1:
        player_result = 1
    elif player_choice == 1 and computer_choice == 2:
        player_result = 0
    elif player_choice == 2 and computer_choice == 3:
        player_result = 0
    elif player_choice == 3 and computer_choice == 1:
        player_result = 0
    elif player_choice == computer_choice:
        player_result = 2

   
def tell_player_result_and_data_count():
    # Function to inform the player of the result and update the round counts
    global win_round
    global total_round
    if player_result == 0:
        print("You lose")
    elif player_result == 2:
        print('It is a tie')
    elif player_result == 1:
        print('You win')
        # Increment win_round if player wins
        win_round += 1
    total_round += 1


def show_data():
    # Function to show the player's win percentage and statistics
    win_percent = (win_round / total_round) * 100
    win_percent = round(win_percent, 2)
    loss_round = total_round - win_round
    print('Your win percent is', win_percent, '%')
    print(f"Your statistics: {total_round} rounds, {win_round} wins, {loss_round} losses")

if __name__ == '__main__':
    # Main game loop
    total_score = 0
    total_round = 0
    win_round = 0
    while True:
        ask_choice()
        player_win_loss()
        tell_player_result_and_data_count()
        if player_result == 0:  # if lose then score -1
            total_score -= 1
        elif player_result == 1:  # if win then score +1
            total_score += 1
        print('Your score is', total_score)
        show_data()
        retry = input('Do you want to continue? (yes/no)')
        if retry != 'yes':
            print('Thank you for playing')
            print('Your final score is', total_score)
            if total_score < 0:
                print('You lost to the computer')
            elif total_score > 0:
                print('You won against the computer')
            elif total_score == 0:
                print('It is a tie overall')
            break