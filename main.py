import random

game_options = list("RPS")

def rock_paper_scissors(players_move,computer):
        if players_move == "R" and computer == "P":
            return "computer won!! Paper covers Rock"
        elif players_move == "P" and computer == "R":
            return "players_move won!! Paper covers Rock"
        elif players_move == "P" and computer == "S":
            return "computer won!! Scissor cuts Paper"
        elif players_move == "S" and computer == "P":
            return "players_move won!! Scissor cuts Paper"
        elif players_move == "R" and computer == "S":
            return "players_move won!! Rock breaks Scissor"
        elif players_move == "S" and computer == "R":
            return "computer won!! Rock breaks Scissor"
        elif players_move not in game_options:
            return "wrong input"
        elif players_move == computer:
            return "Tie"


def play ():
    

    players_move = input("R for rock ,P for Paper,S for scissors : \n").capitalize()
    computer = random.choice(game_options[0:2])


    print(rock_paper_scissors(players_move,computer))
    players_move = input("would you like to play again? y/n \n").capitalize()
    if players_move == "N":
        exit
    elif players_move == "Y":
        play()
    else:
        players_move = input("Wrong input. Try again, Enter y/n \n")
print("Rules of the Game: \n" + "Rock vs Paper -> Paper wins \n" + "Rock vs Scissor -> Rock wins \n" + "Paper vs Scissor -> Scissor wins \n")
play()

