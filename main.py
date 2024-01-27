import random

possible_actions = ["The Rock", "The paper", "The scissor"]

user_score = 6
computer_score = 6

while ((user_score > 0) and (computer_score > 0)):
    computer_action = random.choice(possible_actions)
    # Code logic goes here
    user_Choice = input("play The Rock, The paper or The scissor?")
    print("------------------------------------------")
    print('the computer played:' + computer_action)
    print('the user played: ' + user_Choice)
    print("------------------------------------------")
    if (computer_action == user_Choice):
        print("It's a draw, bois!!!")

    elif (computer_action == "The Rock"):
        if (user_Choice == "The paper"):
            print("you win! YAYY!")
            computer_score -= 1
        elif (computer_action == "The scissor"):
            print("you lose!!! NOOOOO!")
            user_score -= 1


    elif (computer_action == "The scissor"):
        if (user_Choice == "The Rock"):
            print("you win! YAYYY!")
            computer_score -= 1
        elif (user_Choice == "The paper"):
            print("you lose! NOOO!")
            user_score -= 1


    elif (computer_action == "The paper"):
        if (user_Choice == "The scissor"):
            print("you win! YAYYY!")
            computer_score -= 1
        elif (user_Choice == "The Rock"):
            print("you lose! NOOOOOO!")
            user_score -= 1

    # Teacher Code

    print("------------------------------------------")
    print("The computer score is " + str(computer_score))
    print("The user score is " + str(user_score))
    print("------------------------------------------")

if computer_score == 0:
    print("U WIN! YAY!")
elif user_score == 0:
    print("U lose! noooo!")


