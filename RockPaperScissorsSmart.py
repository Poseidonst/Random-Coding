def ask_experience():
    while True:
        question = str(input("Are you experienced (You know the rules and it isn't your first time) ('yes' or 'no')? " ))
        if question == "yes":
            return ("yes")
            break
        elif question == "no":
            return ("no")
            break
        else:
            print ("Invalid input, please try again!")

def ask_gender():
    while True:
        question = str(input("What is your gender ('male' or 'female')? "))
        if question == "male":
            return ("male")
            break
        elif question == "female":
            return ("female")
            break
        else:
            print ("Invalid input, please try again!")

def define_strategy(answer):
    if answer == "yes":
        return ("strat.experienced")
    elif answer == "no":
        return ("strat.rookie")


computerhand_smart(round, prevopp):
    next_move = ""
    if round == 1:
        strat = define_strategy(ask_experience())
        gender = ask_gender()
        if strat == "strat.experienced":
        elif strat == "strat.rookie":
            if gender == "male":
                next_move == "paper"
            elif gender == "female":
                next_move == "rock"
    

    return (next_move)
