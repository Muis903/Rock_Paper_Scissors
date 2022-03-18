from random import choice

list = ['rock', 'paper', 'scissors']

computer = None 
player = None 

while True:
    player = input("\nrock, paper of scissors?: ").lower() 
    computer = choice(list)

    if player == computer:
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("Tie!")
    
    if player == 'paper' and computer == 'rock':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You win")
    
    if player == 'rock' and computer == 'scissors':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You win")

    if player == 'scissors' and computer == 'paper':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You win")
    
    if player == 'scissors' and computer == 'rock':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You lose")
    
    if player == 'rock' and computer == 'paper':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You lose")

    if player == 'paper' and computer == 'scissors':
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("You lose")
    

    play_again = input("\nDo you want to play again? yes/no: ").lower()
    if play_again != "yes":
        break
print("")
