# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("balance: ", balance)
    print ()

    if balance < 1:
        # if balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again " 
                           "or 'xxx' to quit")

   print ()