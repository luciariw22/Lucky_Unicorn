import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or am integer that is more than 0"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0

rounds_lost = 0
rounds_drawn = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), " \
                         "paper (p) or scissors (s) " \
                         "or 'xxx to exit"
    choose_error = "Please choose from rock " \
                   "paper / scissors (or xxx to quit) "

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list,
                            choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice,
                                             comp_choice, result)

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # **** rest of loop / game *****
    print("You chose {}".format(user_choice))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history.
# If 'yes' show game history

# Show Game statistics
# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")
