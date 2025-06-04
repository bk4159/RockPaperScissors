from random import randint

##list of playing options
rps = ["Rock", "Paper", "Scissors"]

##computer gets random choice
computer = rps[randint(0,2)]

player = False
while player == False:
    player = input("Rock, Paper, Scissors? ").strip()
    if player == computer:
        print("The computer is", computer)
        print("Tie!")
    elif player == rps[0]:
        print("The computer is", computer)
        if computer == rps[1]:            
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == rps[1]:
        print("The computer is", computer)
        if computer == rps[2]:
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == rps[2]:
        print("The computer is", computer)
        if computer == rps[0]:
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        #set player to false (to reloop)
        player = False
        continue
    
    ##ask to replay
    invalid = True
    while invalid:
        invalid = input("Play again? Y for yes and N for no. ").lower().strip()
        if invalid == "y":
            player = False
            invalid = False
        elif invalid == "n":
            player = True
            invalid = False
        else:
            print("Invalid input!")
            invalid = True

    computer = rps[randint(0,2)]
