import random
def rock_paper_scissors():
    print("WELCOME! to the infamous Rock Paper Scissor game but this is a digital version of it.")
    print("Let's see if you can beat the computer in this game.")

    player_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    options= ['rock','paper','scissors']
    computer_choice = random.choice(options)

    print(f"\nYou chose {player_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print("It's a tie. Play again!")
    elif(player_choice =='rock' and computer_choice == 'scissors')or(player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        print("CONGRATUALTIONS! You Won!")
    else:
        print("Computer wins! Better luck next time!")        

rock_paper_scissors()
