import random
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice=='rock' and comp_choice=='scissors')or\
    (user_choice=='scissors' and comp_choice=='paper')or\
    (user_choice=='paper' and comp_choice=='rock'):
        return "You win the match!"
    else:
        return "You lose the match!"
def game_play():
    print("Welcome to the game of Rock, Paper, Scissors")
    user_point= 0
    computer_point= 0

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ['rock','paper','scissors']:
            print("Invalid choice. Please choose again.")
            continue 
        computer_choice=random.choice(['rock','paper','scissors'])
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
         
        result=determine_winner(user_choice,computer_choice)
        print(result)
        
        if result=="You win the match!":
            user_point+= 1
        elif result=="You lose the match!":
            computer_point+= 1
        
        print(f"Score - You:{user_point}, Computer:{computer_point}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thankyou for competing!")
            break
            
#Welcome to the game of Rock, Paper, Scissors
#Choose rock, paper, or scissors: rock
#You chose: rock
#Computer chose: rock
#It's a tie!
#Score - You:0, Computer:0
#Do you want to play again? (yes/no): no
#Thankyou for competing!            
